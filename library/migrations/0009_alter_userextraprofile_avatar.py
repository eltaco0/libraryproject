# Generated by Django 4.2.2 on 2023-07-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_userextraprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextraprofile',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to='library/static/avatars/'),
        ),
    ]
