# Generated by Django 2.2.8 on 2020-01-07 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200102_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='330bb04ac83245b98d3d59a8bd41be15b7055b82d1f346178b14313c467af476', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='207000dc6c3f42ceb2d88616cb59b3e20a4f7331f1bd4f38b5ba77c33dc88b88', max_length=300, null=True),
        ),
    ]