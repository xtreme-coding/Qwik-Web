# Generated by Django 3.1.2 on 2021-01-22 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0008_eventregistration_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiftOffCRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('whatsapp_no', models.CharField(max_length=15)),
                ('year', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=100)),
                ('knowledge', models.CharField(max_length=100)),
                ('expectations', models.TextField(blank=True, null=True)),
                ('mode_comm', models.CharField(max_length=10)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='github',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='others',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
