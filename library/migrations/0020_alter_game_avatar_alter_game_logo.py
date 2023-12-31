# Generated by Django 4.2.2 on 2023-07-13 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_game_avatar_game_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='avatar',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='library/static/game/avatar/'),
        ),
        migrations.AlterField(
            model_name='game',
            name='logo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='library/static/game/logo/'),
        ),
    ]
