# Generated by Django 2.0.3 on 2018-04-03 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('blog_count', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
