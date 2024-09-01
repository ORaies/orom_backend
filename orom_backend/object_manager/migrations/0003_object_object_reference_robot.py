# Generated by Django 5.1 on 2024-09-01 12:35

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_library', '0001_initial'),
        ('object_manager', '0002_remove_object_reference_id_remove_robot_object_ptr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='object_reference',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='object_library.referenceobject'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('object_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='object_manager.object')),
                ('joint_angles', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=None)),
                ('robot_reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object_library.referencerobot')),
            ],
            bases=('object_manager.object',),
        ),
    ]
