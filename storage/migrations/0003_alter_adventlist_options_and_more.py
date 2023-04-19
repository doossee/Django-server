# Generated by Django 4.2 on 2023-04-19 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_alter_adventlist_options_alter_client_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adventlist',
            options={'ordering': ['-id', '-created_at'], 'verbose_name': 'Список приходов', 'verbose_name_plural': 'Списки приходов'},
        ),
        migrations.AlterModelOptions(
            name='consumptionlist',
            options={'ordering': ['-id', '-created_at'], 'verbose_name': 'Список расходов', 'verbose_name_plural': 'Списки расходов'},
        ),
        migrations.AlterModelOptions(
            name='profit',
            options={'ordering': ['-id', '-created_at'], 'verbose_name': 'Прибыль', 'verbose_name_plural': 'Прибыли'},
        ),
    ]