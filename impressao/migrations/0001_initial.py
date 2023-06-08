# Generated by Django 4.2.2 on 2023-06-08 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CULTURA', models.CharField(max_length=100)),
                ('PRODUTO_COMERCIAL', models.CharField(max_length=100)),
                ('ALVO', models.CharField(max_length=100)),
                ('AREA_TRATAR', models.CharField(max_length=100)),
                ('VOLUME_CALDA', models.CharField(max_length=100)),
                ('INTERVALO_SEGURANCA', models.CharField(max_length=100)),
                ('MODALIDADE_APLICACAO', models.CharField(max_length=100)),
                ('EQUIPAMENTO_APLICACAO', models.CharField(max_length=100)),
                ('QUANTIDADE_ADQUIRIR', models.CharField(max_length=100)),
                ('NUMERO_APLICACOES', models.CharField(max_length=100)),
                ('EPOCA_APLICACAO', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProdutorRural',
            fields=[
                ('NOME', models.CharField(max_length=100)),
                ('NUM_REGISTRO', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ResponsaveisTecnicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOME', models.CharField(max_length=50)),
                ('CNPJ', models.CharField(max_length=50)),
                ('NUM_REGISTRO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='impressao.produtorrural')),
            ],
        ),
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DESCRICAO', models.CharField(max_length=100)),
                ('CNPJ', models.CharField(max_length=100)),
                ('LATITUDE', models.CharField(max_length=100)),
                ('LONGITUDE', models.CharField(max_length=100)),
                ('LOCAL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='impressao.diagnostico')),
            ],
        ),
        migrations.AddField(
            model_name='produtorrural',
            name='PROPRIEDADE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='impressao.responsaveistecnicos'),
        ),
    ]