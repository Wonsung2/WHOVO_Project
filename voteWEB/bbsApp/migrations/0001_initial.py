# Generated by Django 3.2.5 on 2022-03-14 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(help_text='Post ID', primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('writer_id', models.ForeignKey(db_column='writer_id', help_text='post writer ID', on_delete=django.db.models.deletion.CASCADE, to='userApp.webmember')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(help_text='comment ID', primary_key=True, serialize=False)),
                ('contents', models.TextField()),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(db_column='post', on_delete=django.db.models.deletion.CASCADE, to='bbsApp.post')),
                ('writer_id', models.ForeignKey(db_column='writer_id', help_text='comment writer ID', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='userApp.webmember')),
            ],
        ),
    ]
