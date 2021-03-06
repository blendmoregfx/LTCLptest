# Generated by Django 2.0.3 on 2018-04-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishGradiTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('questionNumber', models.IntegerField()),
                ('question', models.CharField(max_length=250)),
                ('AnsA', models.CharField(max_length=200)),
                ('AnsB', models.CharField(max_length=200)),
                ('AnsC', models.CharField(max_length=200)),
                ('AnsD', models.CharField(max_length=200)),
                ('rightAnswer', models.CharField(max_length=200)),
                ('selectedAns', models.CharField(max_length=200)),
                ('userId', models.CharField(max_length=150)),
                ('userEmail', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='FrenchQuestionandanswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionHead', models.TextField(max_length=4000)),
                ('language', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('questionNumber', models.IntegerField()),
                ('question', models.CharField(max_length=250)),
                ('AnsA', models.CharField(max_length=200)),
                ('AnsB', models.CharField(max_length=200)),
                ('AnsC', models.CharField(max_length=200)),
                ('AnsD', models.CharField(max_length=200)),
                ('rightAnswer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MandarinQuestionandanswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionHead', models.TextField(max_length=4000)),
                ('language', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('questionNumber', models.IntegerField()),
                ('question', models.CharField(max_length=250)),
                ('AnsA', models.CharField(max_length=200)),
                ('AnsB', models.CharField(max_length=200)),
                ('AnsC', models.CharField(max_length=200)),
                ('AnsD', models.CharField(max_length=200)),
                ('rightAnswer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProenglishQuestionsandanswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionHead', models.TextField(max_length=4000)),
                ('language', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('questionNumber', models.IntegerField()),
                ('question', models.CharField(max_length=250)),
                ('AnsA', models.CharField(max_length=200)),
                ('AnsB', models.CharField(max_length=200)),
                ('AnsC', models.CharField(max_length=200)),
                ('AnsD', models.CharField(max_length=200)),
                ('rightAnswer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SwahiliQuestionandanswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionHead', models.TextField(max_length=4000)),
                ('language', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('questionNumber', models.IntegerField()),
                ('question', models.CharField(max_length=250)),
                ('AnsA', models.CharField(max_length=200)),
                ('AnsB', models.CharField(max_length=200)),
                ('AnsC', models.CharField(max_length=200)),
                ('AnsD', models.CharField(max_length=200)),
                ('rightAnswer', models.CharField(max_length=200)),
            ],
        ),
    ]
