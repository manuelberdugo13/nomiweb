# Generated by Django 5.0.4 on 2024-07-02 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_centrotrabajo_ciudades_costos_empvacaciones_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Festivos',
            fields=[
                ('idfestivo', models.IntegerField(primary_key=True, serialize=False)),
                ('dia', models.DateField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=60, null=True)),
                ('ano', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'festivos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ingresosyretenciones',
            fields=[
                ('idingret', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('tipodocumento', models.CharField(blank=True, null=True)),
                ('docidentidad', models.CharField(blank=True, null=True)),
                ('papellido', models.CharField(blank=True, null=True)),
                ('sapellido', models.CharField(blank=True, null=True)),
                ('pnombre', models.CharField(blank=True, null=True)),
                ('snombre', models.CharField(blank=True, null=True)),
                ('salarios', models.IntegerField(blank=True, null=True)),
                ('honorarios', models.IntegerField(blank=True, null=True)),
                ('servicios', models.IntegerField(blank=True, null=True)),
                ('comisiones', models.IntegerField(blank=True, null=True)),
                ('prestacionessociales', models.IntegerField(blank=True, null=True)),
                ('viaticos', models.IntegerField(blank=True, null=True)),
                ('gastosderepresentacion', models.IntegerField(blank=True, null=True)),
                ('compensacioncta', models.IntegerField(blank=True, null=True)),
                ('cesantiasintereses', models.IntegerField(blank=True, null=True)),
                ('pensiones', models.IntegerField(blank=True, null=True)),
                ('totalingresosbrutos', models.IntegerField(blank=True, null=True)),
                ('aportessalud', models.IntegerField(blank=True, null=True)),
                ('aportespension', models.IntegerField(blank=True, null=True)),
                ('aportesvoluntarios', models.IntegerField(blank=True, null=True)),
                ('aportesafc', models.IntegerField(blank=True, null=True)),
                ('retefuente', models.IntegerField(blank=True, null=True)),
                ('anoacumular', models.CharField(blank=True, null=True)),
                ('otrospagos', models.IntegerField(blank=True, null=True)),
                ('fondocesantias', models.IntegerField(blank=True, null=True)),
                ('excesoalim', models.IntegerField(blank=True, null=True)),
                ('cesantias90', models.IntegerField(blank=True, null=True)),
                ('apoyoeconomico', models.IntegerField(blank=True, null=True)),
                ('aportesavc', models.IntegerField(blank=True, null=True)),
                ('ingresolaboralpromedio', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ingresosyretenciones',
                'managed': False,
            },
        ),
    ]
