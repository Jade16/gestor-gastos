# Generated by Django 3.2.22 on 2024-08-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0003_gastos_tipopagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='descricao',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='gastos',
            name='parcelas',
            field=models.IntegerField(),
        ),
    ]
