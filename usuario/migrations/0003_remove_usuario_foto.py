# Generated by Django 5.0.3 on 2024-03-31 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='foto',
        ),
    ]
