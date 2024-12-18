# Generated by Django 5.1.3 on 2024-11-30 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canalizaciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='fecha_creacion',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='fecha',
            field=models.DateField(auto_now_add=True, default='2024-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='alumno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='tipo',
            field=models.CharField(choices=[('beca', 'Beca'), ('asesoria', 'Asesoría'), ('psicologia', 'Atención Psicológica')], max_length=20),
        ),
    ]
