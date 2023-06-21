# Generated by Django 4.1.3 on 2023-05-09 15:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='address',
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
