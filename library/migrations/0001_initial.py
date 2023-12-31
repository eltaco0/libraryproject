# Generated by Django 4.2.2 on 2023-06-28 17:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('release', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserOwnedGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserExtraProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=35, unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GamePublisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.game')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='GameGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.game')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.genre')),
            ],
        ),
        migrations.CreateModel(
            name='GameDeveloper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.developer')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ManyToManyField(through='library.GameDeveloper', to='library.developer'),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(through='library.GameGenre', to='library.genre'),
        ),
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.ManyToManyField(through='library.GamePublisher', to='library.publisher'),
        ),
    ]
