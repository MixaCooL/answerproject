# Generated by Django 3.0.1 on 2019-12-22 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Goods_name')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Section_name')),
            ],
        ),
        migrations.CreateModel(
            name='ViewsSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Section_name')),
                ('ip', models.CharField(max_length=30, verbose_name='User_ip')),
                ('datetime', models.DateTimeField(verbose_name='DateTime_action')),
                ('id_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_report.Section', verbose_name='Section_id')),
            ],
        ),
    ]
