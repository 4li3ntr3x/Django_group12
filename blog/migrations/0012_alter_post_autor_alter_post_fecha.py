# Generated by Django 4.1.3 on 2023-11-09 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_autor_alter_post_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]