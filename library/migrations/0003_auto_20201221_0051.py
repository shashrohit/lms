# Generated by Django 3.0a1 on 2020-12-20 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20201221_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='due_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_issued',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='issued_to',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Users'),
        ),
    ]
