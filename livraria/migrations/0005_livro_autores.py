# Generated by Django 5.0.3 on 2024-03-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0004_alter_livro_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(related_name='livros', to='livraria.autor'),
        ),
    ]