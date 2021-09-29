# Generated by Django 3.2.4 on 2021-09-13 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(upload_to='product')),
                ('name', models.CharField(max_length=264)),
                ('preview_text', models.TextField(max_length=200, verbose_name='Preview Text')),
                ('details_text', models.TextField(max_length=1000, verbose_name='Description')),
                ('price', models.FloatField()),
                ('old_price', models.FloatField(default=0.0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='App_Shop.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
