# Generated by Django 3.2.4 on 2021-06-30 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField()),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Boletas',
            fields=[
                ('numero', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('total', models.FloatField()),
                ('mediopago', models.CharField(max_length=50)),
                ('fecha_compromiso', models.DateField()),
            ],
            options={
                'db_table': 'boletas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
            ],
            options={
                'db_table': 'clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField()),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('codigo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('secuencia', models.BigIntegerField()),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'familia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kardex',
            fields=[
                ('correlativo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('cod_producto', models.CharField(max_length=10)),
                ('entrada', models.FloatField()),
                ('salida', models.FloatField()),
                ('numero_boleta', models.BigIntegerField()),
            ],
            options={
                'db_table': 'kardex',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oc',
            fields=[
                ('codigo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('fecha_recepcion', models.DateField()),
                ('total', models.FloatField()),
            ],
            options={
                'db_table': 'oc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('secuencia', models.BigIntegerField()),
                ('rut_proveedor', models.CharField(max_length=9)),
                ('codigo_barra', models.BigIntegerField()),
                ('fecha_vencimiento', models.DateField()),
                ('descripcion', models.CharField(max_length=50)),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.FloatField()),
                ('stock', models.FloatField()),
                ('stock_critico', models.FloatField()),
                ('imagen', models.BinaryField()),
            ],
            options={
                'db_table': 'productos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('secuencia', models.BigIntegerField()),
                ('razon_social', models.CharField(max_length=50)),
                ('giro', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
                ('contacto', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'proveedores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecOc',
            fields=[
                ('cod_oc', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('estado', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'rec_oc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'unidad_medida',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BoletaDetalle',
            fields=[
                ('numero_boleta', models.OneToOneField(db_column='numero_boleta', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.boletas')),
                ('secuencia', models.BigIntegerField()),
                ('cantidad', models.FloatField()),
                ('precio', models.FloatField()),
            ],
            options={
                'db_table': 'boleta_detalle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CuentasCorrientes',
            fields=[
                ('rut_cliente', models.OneToOneField(db_column='rut_cliente', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.clientes')),
                ('secuencia', models.BigIntegerField()),
                ('fecha', models.DateField()),
                ('fecha_compromiso', models.DateField()),
                ('cargo', models.FloatField()),
                ('abono', models.FloatField()),
                ('estado', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cuentas_corrientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OcDetalle',
            fields=[
                ('cod_oc', models.OneToOneField(db_column='cod_oc', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.oc')),
                ('secuencia', models.BigIntegerField()),
                ('cantidad', models.FloatField()),
                ('precio_unitario', models.FloatField()),
            ],
            options={
                'db_table': 'oc_detalle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecOcDetalle',
            fields=[
                ('cod_oc', models.OneToOneField(db_column='cod_oc', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.recoc')),
                ('secuencia', models.BigIntegerField()),
                ('cantidad', models.FloatField()),
                ('pendiente', models.FloatField()),
            ],
            options={
                'db_table': 'rec_oc_detalle',
                'managed': False,
            },
        ),
    ]