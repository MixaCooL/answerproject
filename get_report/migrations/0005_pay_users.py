# Generated by Django 3.0.1 on 2019-12-22 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_report', '0004_auto_20191222_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.CharField(max_length=30, verbose_name='Id_user')),
            ],
        ),
        migrations.CreateModel(
            name='pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='User_ip')),
                ('datetime', models.DateTimeField(verbose_name='DateTime_pay')),
                ('id_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_report.Cart', verbose_name='Id_cart')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_report.Users', verbose_name='Id_user')),
            ],
        ),
    ]
