# Generated by Django 3.2.12 on 2022-10-18 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='College.mybasemodel')),
                ('ten', models.IntegerField()),
                ('tweleve', models.IntegerField()),
                ('science', models.IntegerField()),
                ('arts', models.IntegerField()),
                ('commerce', models.IntegerField()),
                ('principle', models.IntegerField()),
            ],
            bases=('College.mybasemodel',),
        ),
    ]
