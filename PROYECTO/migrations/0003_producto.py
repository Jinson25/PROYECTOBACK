# Generated by Django 4.1 on 2022-08-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PROYECTO', '0002_remove_post_slug_remove_post_likes_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('categoria', models.CharField(max_length=32)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
