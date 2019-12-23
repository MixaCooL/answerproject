from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=30,verbose_name='Goods_name')
    id_goods = models.CharField(max_length=30,verbose_name='Id_name')

    def __str__(self):
        return self.id_goods

class Users(models.Model):
    id_user = models.CharField(max_length=30,verbose_name='Id_user')

    def __str__(self):
        return self.id_user

class Section(models.Model):
    name = models.CharField(max_length=30,verbose_name='Section_name')

    def __str__(self):
        return self.name

class ViewsSection(models.Model):
    section = models.ForeignKey(Section,on_delete=models.CASCADE,verbose_name='Section_name')
    ip = models.CharField(max_length=30,verbose_name='User_ip')
    datetime = models.DateTimeField(verbose_name='DateTime_action')

    #def __str__(self):
    #    return self.section

class ViewsGoods(models.Model):
    name = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='Goods_name')
    ip = models.CharField(max_length=30,verbose_name='User_ip')
    datetime = models.DateTimeField(verbose_name='DateTime_action')

    #def __str__(self):
    #    return self.name

class Cart(models.Model):
    id_cart = models.CharField(max_length=30,verbose_name='Id_cart')
    ip = models.CharField(max_length=30,verbose_name='User_ip')

    def __str__(self):
        return self.id_cart

class AddGoods_in_cart(models.Model):
    name = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='Goods_name')
    id_cart = models.ForeignKey(Cart,on_delete=models.CASCADE,verbose_name='Id_cart')
    ip = models.CharField(max_length=30,verbose_name='User_ip')
    datetime = models.DateTimeField(verbose_name='DateTime_action')
    amount = models.IntegerField(verbose_name='Amount')

    #def __str__(self):
    #    return self.name

class Pay(models.Model):
    id_user = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='Id_user')
    id_cart = models.ForeignKey(Cart,on_delete=models.CASCADE,verbose_name='Id_cart')
    ip = models.CharField(max_length=30,verbose_name='User_ip')
    datetime = models.DateTimeField(verbose_name='DateTime_pay')

    #def __str__(self):
    #    return self.id_user