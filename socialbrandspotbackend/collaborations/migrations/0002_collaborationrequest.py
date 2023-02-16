# Generated by Django 4.1.7 on 2023-02-16 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
        ('influencers', '0002_influencer_delete_profile'),
        ('collaborations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollaborationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collaboration_requests', to='brands.brand')),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collaboration_requests', to='influencers.influencer')),
            ],
        ),
    ]
