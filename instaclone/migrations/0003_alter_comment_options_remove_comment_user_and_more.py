# Generated by Django 4.0.3 on 2022-04-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0002_profile_bio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=True),
        ),
    ]
