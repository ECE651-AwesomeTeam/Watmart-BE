# Generated by Django 4.1.6 on 2023-02-10 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('fname', models.CharField(max_length=16)),
                ('lname', models.CharField(max_length=16)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('wat_id', models.CharField(blank=True, max_length=8, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('STU', 'Student'), ('FAC', 'Faculty')], max_length=3, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backbone.user')),
                ('md5_pwd', models.CharField(max_length=32)),
            ],
        ),
    ]
