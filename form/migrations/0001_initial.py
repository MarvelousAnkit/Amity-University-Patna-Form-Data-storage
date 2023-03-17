# Generated by Django 4.1.7 on 2023-02-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summary2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch', models.CharField(max_length=100)),
                ('Program', models.CharField(max_length=100)),
                ('Semester', models.CharField(max_length=300)),
                ('Course_Title', models.CharField(max_length=300)),
                ('Course_Unit', models.CharField(max_length=100)),
                ('Course_Level', models.CharField(max_length=100)),
                ('Course_Code', models.CharField(max_length=100)),
                ('Course_Objective', models.CharField(max_length=2000)),
                ('Course_Content', models.CharField(max_length=100)),
                ('Course_Weightage', models.CharField(max_length=100)),
                ('Student_Learning_Outcome', models.CharField(max_length=3000)),
                ('Pedagogy', models.CharField(max_length=2000)),
            ],
        ),
    ]