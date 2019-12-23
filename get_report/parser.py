import pandas as pd
import json
import re 
import numpy as np
from .models import *
import datetime as dt
from datetime import datetime, date, time

def result():
    pattern_goods = '^https:\/\/all_to_the_bottom\.com\/([\w]*)\/([\w]*)\/$'
    pattern_section = '^https:\/\/all_to_the_bottom\.com\/([\w]*)\/$'
    pattern_pay = 'https:\/\/all_to_the_bottom\.com\/success_pay_([0-9]*)'
    pattern_prepay = 'https://all_to_the_bottom\.com/pay\?user_id=([\d]*)'
    pattern_cart = '^https://all_to_the_bottom\.com/cart\?goods_id=([0-9]*)&amount=([0-9]{1,5})&cart_id=([0-9]*)$'

    path = 'D:\\Program Files\\is74\\logs.txt'
    df = pd.read_csv(path, sep='\s+',names=['test0','test','date','time','key','delet','ip','link'])
    del df['test0']
    del df['test']
    del df['delet']

    df_ip = df['ip'].drop_duplicates().reset_index(drop=True)
    index = 0
    for ip in df_ip['ip']:
        df_info = df.loc[df['ip'].isin([ip])].reset_index(drop=True)
        i= 0
        for link in df_info['link']:
            if re.search(pattern_cart, link):
                if not Section.objects.filter(name = re.search(pattern_goods,df_info['link'][i-1]).group(1)):
                    Section(name = re.search(pattern_goods,df_info['link'][i-1]).group(1)).save()
                if not Goods.objects.filter(name = re.search(pattern_goods,df_info['link'][i-1]).group(2)):
                    Goods(name = re.search(pattern_goods,df_info['link'][i-1]).group(2)).save()
                if not Cart.objects.filter(id_cart = re.search(pattern_cart,df_info['link'][i]).group(3)):
                    Cart(id_cart = re.search(pattern_cart,df_info['link'][i]).group(3),ip=df_info['ip'][i]).save()
                index +=1
            if re.search(pattern_pay, link):
                if not Users.objects.filter(id_user = re.search(pattern_prepay,df_info['link'][i-1]).group(1)):
                    Users(id_user = re.search(pattern_prepay,df_info['link'][i-1]).group(1)).save()
            i+=1

def result_other_views():
    pattern_goods = '^https:\/\/all_to_the_bottom\.com\/([\w]*)\/([\w]*)\/$'
    pattern_section = '^https:\/\/all_to_the_bottom\.com\/([\w]*)\/$'
    pattern_pay = 'https:\/\/all_to_the_bottom\.com\/success_pay_([0-9]*)'
    pattern_prepay = 'https://all_to_the_bottom\.com/pay\?user_id=([\d]*)'
    pattern_cart = '^https://all_to_the_bottom\.com/cart\?goods_id=([0-9]*)&amount=([0-9]{1,5})&cart_id=([0-9]*)$'

    path = 'D:\\Program Files\\is74\\logs.txt'
    df = pd.read_csv(path, sep='\s+',names=['test0','test','date','time','key','delet','ip','link'])
    del df['test0']
    del df['test']
    del df['delet']

    df_ip = df['ip'].drop_duplicates().reset_index(drop=True)
    for ip in df_ip['ip']:
        df_info = df.loc[df['ip'].isin([ip])].reset_index(drop=True)
        i= 0
        for link in df_info['link']:
            if re.search(pattern_section, link):
                name_section = re.search(pattern_section,df_info['link'][i]).group(1)
                if Section.objects.filter(name = name_section):
                    ViewsSection(section= Section.objects.get(name=name_section),ip = df_info['ip'][i],datetime = str(df_info['date'][i]) +' ' +str(df_info['time'][i])).save()
                name_goods = re.search(pattern_goods,df_info['link'][i]).group(2)
                if Goods.objects.filter(name = name_goods):
                    ViewsGoods(name= Goods.objects.get(name=name_goods),ip = df_info['ip'][i],datetime = str(df_info['date'][i]) +' ' +str(df_info['time'][i])).save()
            i+=1

def result__pay_and_action():
    pattern_goods = '^https:\/\/all_to_the_bottom\.com\/([\w]*)\/([\w]*)\/$'
    pattern_section = '^https:\/\/all_to_the_bottom\.com\/([\w]*)\/$'
    pattern_pay = 'https:\/\/all_to_the_bottom\.com\/success_pay_([0-9]*)'
    pattern_prepay = 'https://all_to_the_bottom\.com/pay\?user_id=([\d]*)'
    pattern_cart = '^https://all_to_the_bottom\.com/cart\?goods_id=([0-9]*)&amount=([0-9]{1,5})&cart_id=([0-9]*)$'

    path = 'D:\\Program Files\\is74\\logs.txt'
    df = pd.read_csv(path, sep='\s+',names=['test0','test','date','time','key','delet','ip','link'])
    del df['test0']
    del df['test']
    del df['delet']

    df_ip = df['ip'].drop_duplicates().reset_index(drop=True)
    for ip in df_ip:
        df_info = df.loc[df['ip'].isin([ip])].reset_index(drop=True)
        i= 0
        for link in df_info['link']:
            if re.search(pattern_cart, link):
                id_goods = re.search(pattern_cart,df_info['link'][i]).group(1)
                amount = re.search(pattern_cart,df_info['link'][i]).group(2)
                id_cart = re.search(pattern_cart,df_info['link'][i]).group(3)
                AddGoods_in_cart(name= Goods.objects.get(id_goods = id_goods),ip = df_info['ip'][i],datetime = str(df_info['date'][i]) +' ' +str(df_info['time'][i]),id_cart=Cart.objects.get(id_cart = id_cart),amount=amount).save()
            if re.search(pattern_pay, link):
                id_cart = re.search(pattern_pay,df_info['link'][i]).group(1)
                id_user = re.search(pattern_prepay,df_info['link'][i-1]).group(1)
                Pay(id_user= Users.objects.get(id_user = id_user),id_cart=Cart.objects.get(id_cart = id_cart),ip = df_info['ip'][i],datetime = str(df_info['date'][i]) +' ' +str(df_info['time'][i])).save()
            i+=1