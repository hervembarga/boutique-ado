# Generated by Django 3.1.7 on 2021-04-28 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20210428_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordertwo',
            old_name='product',
            new_name='producttwo',
        ),
        migrations.RemoveField(
            model_name='ordertwo',
            name='grand_total',
        ),
    ]
