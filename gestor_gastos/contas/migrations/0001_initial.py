# Generated by Django 3.2.22 on 2024-08-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('origem', models.CharField(max_length=255)),
                ('dataVencimento', models.DateField()),
                ('tipoConta', models.CharField(blank=True, choices=[('A', 'Aluguel'), ('G', 'Água'), ('L', 'Luz'), ('I', 'Internet'), ('O', 'Outros')], max_length=1, null=True)),
            ],
        ),
    ]
