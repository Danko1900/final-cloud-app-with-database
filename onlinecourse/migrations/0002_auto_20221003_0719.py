# Generated by Django 3.1.3 on 2022-10-03 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='choice',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='lesson',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='grade',
        ),
    ]
