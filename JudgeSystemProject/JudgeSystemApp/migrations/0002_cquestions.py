# Generated by Django 3.2.8 on 2021-11-16 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JudgeSystemApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=300)),
                ('difficulty', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('long_description', models.CharField(default='no heading', max_length=700)),
                ('accuracy', models.FloatField(default='90.9')),
                ('example_1', models.OneToOneField(default='no heading', on_delete=django.db.models.deletion.CASCADE, related_name='example1', to='JudgeSystemApp.example')),
                ('example_2', models.OneToOneField(default='no heading', on_delete=django.db.models.deletion.CASCADE, related_name='example2', to='JudgeSystemApp.example')),
            ],
        ),
    ]
