# Generated by Django 4.0.5 on 2022-12-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_contact_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_me',
            name='Country',
            field=models.CharField(choices=[('dubai', 'DUBAI'), ('seychelles', 'SEYCHELLES'), ('singapore', 'SINGAPORE')], default='Select', max_length=15),
        ),
    ]
