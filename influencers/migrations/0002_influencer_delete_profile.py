# Generated by Django 4.1.7 on 2023-02-16 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Influencer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('instagram_handle', models.CharField(blank=True, max_length=30, null=True)),
                ('youtube_channel', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_handle', models.CharField(blank=True, max_length=30, null=True)),
                ('facebook_page', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
