# Generated by Django 4.2.2 on 2023-06-08 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('impressao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnostico',
            name='id',
        ),
        migrations.RemoveField(
            model_name='propriedade',
            name='id',
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='NUM',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produtorrural',
            name='PROPRIEDADE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='impressao.responsaveistecnicos'),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='CNPJ',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='LOCAL',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='impressao.diagnostico'),
        ),
        migrations.AlterField(
            model_name='responsaveistecnicos',
            name='NUM_REGISTRO',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='impressao.produtorrural'),
        ),
    ]