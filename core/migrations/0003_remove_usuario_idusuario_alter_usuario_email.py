# Generated by Django 5.1.5 on 2025-01-26 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usuario_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='idUsuario',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Email'),
        ),
    ]
