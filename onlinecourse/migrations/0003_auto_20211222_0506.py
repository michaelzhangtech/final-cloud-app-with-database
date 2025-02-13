# Generated by Django 3.1.3 on 2021-12-22 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_choice_seqno'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='content',
            field=models.CharField(default='title', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.CharField(default='title', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='title', max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='result',
            field=models.BooleanField(default=True),
        ),
    ]
