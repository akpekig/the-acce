# Generated by Django 3.2.9 on 2021-11-29 17:25

import datetime
from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Matter',
            fields=[
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Enter the title of the matter. Keep it short.', max_length=64)),
                ('description', models.CharField(help_text="Describe the matter. Don't make it complex.", max_length=512)),
                ('cost_type', models.CharField(choices=[('P', 'Price'), ('R', 'Rate')], default='P', help_text='Select the type of cost you will charge.', max_length=1)),
                ('amount', models.DecimalField(decimal_places=2, default=0, help_text='Include all costs related to the matter.', max_digits=6, validators=[django.core.validators.MinValueValidator(Decimal('0.00')), django.core.validators.MaxValueValidator(Decimal('9999.99'))])),
                ('estimated_hours', models.DecimalField(decimal_places=2, default=5, help_text='Approximate how many hours you will work.', max_digits=6, validators=[django.core.validators.MinValueValidator(Decimal('0.00')), django.core.validators.MaxValueValidator(Decimal('9999.99'))])),
                ('logged_hours', models.DecimalField(decimal_places=2, default=0, help_text="Approximate how many hours you have worked. This can not exceed estimated hours without your client's permission.", max_digits=6, validators=[django.core.validators.MinValueValidator(Decimal('0.00')), django.core.validators.MaxValueValidator(Decimal('9999.99'))])),
                ('start_date', models.DateField(default=datetime.date.today, help_text='When should the client expect you to start working?')),
                ('due_date', models.DateField(blank=True, null=True)),
                ('has_client_permission', models.BooleanField(default=False, verbose_name="Do you have your client's explicit permission to begin immediately?")),
                ('has_external_services', models.BooleanField(default=False, verbose_name='Do you need to involve external services in this matter?')),
                ('has_client_pre_tasks', models.BooleanField(default=False, verbose_name='Does the client need to carry out any tasks before you begin?')),
                ('has_related_articles', models.BooleanField(default=False, verbose_name='Does the client need to know any extra information?')),
                ('is_changeable', models.BooleanField(default=False, verbose_name='Do you want to change the cost in the future?')),
                ('is_active', models.BooleanField(default=True)),
                ('client_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matters.client')),
                ('lawyer_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matters.lawyer')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Pretask',
            fields=[
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=256)),
                ('is_complete', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('matter_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pretask', related_query_name='pretasks', to='matters.matter')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('company', models.CharField(blank=True, max_length=64, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=64, null=True)),
                ('website', models.CharField(blank=True, max_length=128, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='matters.location')),
                ('matter_key', models.ManyToManyField(related_name='external_contact', related_query_name='external_contacts', to='matters.Matter')),
            ],
        ),
    ]