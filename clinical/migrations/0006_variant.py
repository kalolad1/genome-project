# Generated by Django 2.1.3 on 2018-12-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinical', '0005_auto_20181212_0341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_id', models.CharField(max_length=50)),
                ('gene_name', models.CharField(max_length=100)),
                ('phenotype_list', models.CharField(max_length=200)),
                ('start', models.IntegerField()),
                ('stop', models.IntegerField()),
                ('clinical_significance', models.CharField(max_length=200)),
                ('chromosome', models.IntegerField()),
                ('reference_allele', models.CharField(max_length=1)),
                ('alternate_allele', models.CharField(max_length=1)),
            ],
        ),
    ]
