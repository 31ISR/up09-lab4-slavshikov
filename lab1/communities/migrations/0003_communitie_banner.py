# Generated by Django 4.2.17 on 2024-12-17 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_rename_communities_communitie'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitie',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]
