# Generated by Django 2.2.7 on 2019-11-14 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=150)),
                ('flag', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('confirm', models.BooleanField(default=False)),
                ('confirmation_date', models.DateTimeField(blank=True, null=True)),
                ('application_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('account', models.FloatField(default=0)),
                ('refferal_level_income', models.FloatField(default=0)),
                ('level_income', models.FloatField(default=0)),
                ('user_activation', models.BooleanField(default=False)),
                ('btc_activation', models.BooleanField(default=False)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='member.Country')),
                ('sponsor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsored', to='member.UserProfileInfo')),
                ('user_profile', models.OneToOneField(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WithdrawalHistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_address', models.CharField(blank=True, max_length=250, null=True)),
                ('ammount', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.UserProfileInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Histry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(blank=True, max_length=250, null=True)),
                ('date_of_activation', models.DateTimeField(blank=True, null=True)),
                ('level_income', models.FloatField(blank=True, null=True)),
                ('level_income_date', models.DateTimeField(blank=True, null=True)),
                ('refferal_level_income', models.FloatField(blank=True, null=True)),
                ('refferal_level_income_date', models.DateTimeField(blank=True, null=True)),
                ('invoice_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('reward', models.CharField(blank=True, max_length=250, null=True)),
                ('rewarded_date', models.DateTimeField(blank=True, null=True)),
                ('withdrawal', models.FloatField(blank=True, null=True)),
                ('withdrawal_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.UserProfileInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('level_status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.UserProfileInfo')),
            ],
        ),
    ]
