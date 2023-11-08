# Generated by Django 4.1 on 2023-10-24 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comentario_contenido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='etiquetas',
            field=models.ManyToManyField(to='blog.etiqueta'),
        ),
    ]