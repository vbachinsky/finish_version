# Generated by Django 2.2.8 on 2020-01-20 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='220eda29b6854f108c3607bb1ae6e9e5db3841a4a2a8486d99bdbd7e5204b605', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='348a52ac503b4544874d1936f82ddd8c32930c9362c44692a7f2541739f75dfe', max_length=300, null=True),
        ),
    ]
