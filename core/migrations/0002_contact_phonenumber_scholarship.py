# Generated by Django 3.0.8 on 2020-07-18 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(default='')),
                ('details', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, default='', max_length=50)),
                ('fax', models.CharField(blank=True, default='', max_length=255)),
                ('website', models.CharField(blank=True, default='', max_length=255)),
                ('position', models.CharField(blank=True, default='', max_length=60)),
                ('phone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.PhoneNumber')),
            ],
        ),
    ]
