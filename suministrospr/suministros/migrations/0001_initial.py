# Generated by Django 2.2.9 on 2020-01-13 22:09

from django.db import migrations, models
import django.utils.timezone
import suministrospr.utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suministro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', suministrospr.utils.fields.DateTimeCreatedField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', suministrospr.utils.fields.DateTimeModifiedField(default=django.utils.timezone.now, editable=False)),
                ('title', models.CharField(max_length=255)),
                ('municipality', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ('-modified_at', '-created_at'),
                'get_latest_by': 'modified_at',
                'abstract': False,
            },
        ),
    ]