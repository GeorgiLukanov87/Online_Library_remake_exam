# Generated by Django 4.2.2 on 2023-06-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_web', '0002_alter_bookmodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='type',
            field=models.CharField(choices=[('Fiction', '1.Fiction'), ('Novel', '2.Novel'), ('Crime', '3.Crime'), ('Fantasy', '4.Fantasy'), ('Roman', '5.Roman'), ('Study', '6.Study'), ('Modern', '7.Modern'), ('Horror', '8.Horror')], max_length=20),
        ),
    ]