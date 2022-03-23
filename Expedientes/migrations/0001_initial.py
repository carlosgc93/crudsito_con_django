# Generated by Django 4.0 on 2021-12-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registroExpediente',
            fields=[
                ('numNue', models.IntegerField(primary_key=True, serialize=False)),
                ('numNut', models.IntegerField()),
                ('numExpediente', models.IntegerField()),
                ('fechaApertura', models.DateField()),
                ('nombre', models.CharField(max_length=150)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('fechaNacimiento', models.DateField()),
            ],
        ),
    ]