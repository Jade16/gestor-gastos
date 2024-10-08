# Generated by Django 3.2.22 on 2024-08-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('origem', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('M', 'Mercado'), ('S', 'Saúde'), ('L', 'Laser'), ('T', 'Transporte'), ('A', 'Alimentação')], max_length=1)),
                ('data', models.DateField()),
                ('descricao', models.CharField(max_length=500)),
                ('repeticao', models.CharField(blank=True, choices=[('Q', 'Quinzenal'), ('S', 'Semanal'), ('M', 'Mensal'), ('N', 'Não se repete')], max_length=1, null=True)),
            ],
        ),
    ]
