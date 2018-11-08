# Generated by Django 2.1.3 on 2018-11-08 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'remanent',
                'verbose_name_plural': 'remanenty',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='cena brutto')),
                ('quantity', models.FloatField(verbose_name='ilość')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('inventory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Inventory', verbose_name='remanent')),
            ],
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='nazwa towaru')),
                ('name_print', models.CharField(max_length=70, null=True, verbose_name='nazwa do druku')),
            ],
        ),
        migrations.CreateModel(
            name='MakeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='nazwa grupy towarowej')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='sklep')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='make',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.MakeGroup', verbose_name='grupa towarowa'),
        ),
        migrations.AddField(
            model_name='item',
            name='make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Make', verbose_name='nazwa towaru'),
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Unit', verbose_name='j.m.'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Shop', verbose_name='sklep'),
        ),
    ]