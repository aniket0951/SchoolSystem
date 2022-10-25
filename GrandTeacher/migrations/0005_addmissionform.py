# Generated by Django 3.2.12 on 2022-10-21 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0004_alter_practicalroom_electronics'),
        ('GrandTeacher', '0004_subsubject'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddmissionForm',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='College.mybasemodel')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('middel_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('ten_persentage', models.IntegerField()),
                ('twelve_persentage', models.IntegerField()),
                ('addmission_fee', models.IntegerField()),
            ],
            bases=('College.mybasemodel',),
        ),
    ]