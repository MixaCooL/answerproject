from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
#from .parser import result__pay_and_action
from .models import *
from datetime import datetime,time
import pandas as pd
import json
import requests
#from geoip import geolite2
from geolite2 import geolite2

def get_country(ip):
    reader = geolite2.reader()
    try:
        country = reader.get(ip)['country']['names']['ru']
    except TypeError:
        country = 'Не найдено'
    except KeyError:
        country = reader.get(ip)['registered_country']['names']['ru']
    return country
def switch_times_of_day(time_df):
    return {
    time(4, 00)<time_df<= time(11, 00) : 'утром',
    time(11, 00)<time_df<= time(16, 00) : 'днем',
    time(16, 00)<time_df<= time(23, 59, 59) : 'вечером',
    time(00, 00)<=time_df<= time(4, 00) : 'ночью',
    }[True]    
def report(request):
    if request.method == "POST":
        if request.headers['action'] == 'top_country':
            index = 0
            response = dict()
            df = pd.DataFrame({
                'ip':[],
            })
            items = request.POST
            all_action_viewsSection = ViewsSection.objects.all()
            for ip in all_action_viewsSection:
                df.loc[index,'ip'] = ip.ip
                index +=1
            all_action_viewsGoods = ViewsGoods.objects.all()
            for ip in all_action_viewsGoods:
                df.loc[index,'ip'] = ip.ip
                index +=1
            all_action_cart = AddGoods_in_cart.objects.all()
            for ip in all_action_cart:
                df.loc[index,'ip'] = ip.ip
                index +=1
            df = df['ip'].drop_duplicates().reset_index()
            del df['index']
            df['country'] = df['ip'].apply(get_country)
            geolite2.close()
            df_sup = df['country'].value_counts().to_frame()
            print(df_sup)
            if len(df_sup) < int(items['count']):
                count = len(df_sup)
            else:
                count = items['count']
            for i in range(int(count)):
                response[df_sup.index[i]] = str(df_sup.country[i])
            return HttpResponse(json.dumps(response),content_type="application/json")
        if request.headers['action'] == 'category_country':
            index = 0
            response = dict()
            df = pd.DataFrame({
                'ip':[],
            })
            items = request.POST
            action_views = ViewsSection.objects.filter(section = items['category'])
            for ip in action_views:
                df.loc[index,'ip'] = ip.ip
                index +=1
            df = df['ip'].drop_duplicates().reset_index()
            del df['index']
            df['country'] = df['ip'].apply(get_country)
            print(df)
            df_sup = df['country'].value_counts().to_frame()
            response['Country'] = str(df_sup.index[0])
            response['Count'] = str(df_sup.country[0])
            return HttpResponse(json.dumps(response),content_type="application/json")
        if request.headers['action'] == 'times_of_day':
            items = request.POST
            action_views = ViewsSection.objects.filter(section = items['category'])
            index = 0
            response = dict()
            df = pd.DataFrame({
                'time':[],
            })
            for action in action_views:
                df.loc[index,'time'] = action.datetime.time()
                index +=1
            df['times_of_day'] = df['time'].apply(switch_times_of_day)
            response['times_of_day'] =df['times_of_day'].value_counts().index[0]
            response['category'] = str(Section.objects.filter(id = items['category'])[0])
            return HttpResponse(json.dumps(response),content_type="application/json")
    return render(request, 'report.html')

