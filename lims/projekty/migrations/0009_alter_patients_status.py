# Generated by Django 5.0.6 on 2024-06-21 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekty', '0008_experiments_status_alter_patients_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='status',
            field=models.CharField(choices=[('deceased', 'Deceased'), ('alive', 'Alive'), ('cured', 'Cured')], default='ongoing', max_length=10),
        ),
    ]
