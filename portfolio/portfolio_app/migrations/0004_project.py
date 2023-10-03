# Generated by Django 4.2.5 on 2023-10-03 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_alter_portfolio_about_alter_portfolio_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('portfolio', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio')),
            ],
        ),
    ]
