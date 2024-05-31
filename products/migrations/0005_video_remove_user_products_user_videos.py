# Generated by Django 5.0.6 on 2024-05-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_name_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='products',
        ),
        migrations.AddField(
            model_name='user',
            name='videos',
            field=models.ManyToManyField(null=True, to='products.video'),
        ),
    ]
