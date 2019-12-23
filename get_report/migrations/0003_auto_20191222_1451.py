# Generated by Django 3.0.1 on 2019-12-22 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_report', '0002_auto_20191222_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cart', models.IntegerField(verbose_name='Id_cart')),
                ('ip', models.CharField(max_length=30, verbose_name='User_ip')),
            ],
        ),
        migrations.RenameField(
            model_name='viewssection',
            old_name='id_section',
            new_name='section',
        ),
        migrations.CreateModel(
            name='ViewsGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='User_ip')),
                ('datetime', models.DateTimeField(verbose_name='DateTime_action')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_report.Goods', verbose_name='Goods_name')),
            ],
        ),
        migrations.CreateModel(
            name='AddGoods_in_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='User_ip')),
                ('datetime', models.DateTimeField(verbose_name='DateTime_action')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('id_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_report.Cart', verbose_name='Id_cart')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_report.Goods', verbose_name='Goods_name')),
            ],
        ),
    ]