# Generated by Django 4.1.7 on 2023-02-16 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('influencers', '0002_influencer_delete_profile'),
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaboration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collaborations', to='brands.brand')),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collaborations', to='influencers.influencer')),
            ],
        ),
    ]
