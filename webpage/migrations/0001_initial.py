# Generated by Django 3.1.2 on 2021-01-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('year', models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth')], max_length=6)),
                ('profile_pic', models.ImageField(default='default.jpg', upload_to='member_profile_pic')),
            ],
        ),
    ]