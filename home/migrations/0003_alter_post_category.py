# Generated by Django 4.1.3 on 2022-11-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('general', 'General'), ('python', 'Python'), ('javascript', 'JavaScript'), ('C++', 'C++')], default='general', max_length=150),
        ),
    ]
