# Generated by Django 4.1.7 on 2023-03-24 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_featuredbook_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredbook',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='featured_book_instances', to='core.book'),
        ),
    ]
