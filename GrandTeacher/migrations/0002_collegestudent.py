# Generated by Django 3.2.12 on 2022-10-20 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0002_department'),
        ('GrandTeacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeStudent',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='College.mybasemodel')),
                ('full_name', models.CharField(blank=True, max_length=100)),
                ('std_address', models.CharField(blank=True, max_length=100)),
                ('classroom', models.IntegerField()),
                ('roll_no', models.IntegerField()),
                ('division', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
            bases=('College.mybasemodel',),
        ),
    ]