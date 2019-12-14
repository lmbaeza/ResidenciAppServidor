# Generated by Django 2.2.6 on 2019-12-13 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentHousing', '0004_auto_20191128_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='residencepublication',
            name='address',
        ),
        migrations.RemoveField(
            model_name='residencepublication',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='residencepublication',
            name='neighborhood',
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=255)),
                ('locality', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=64)),
                ('publication', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='StudentHousing.ResidencePublication')),
            ],
        ),
    ]
