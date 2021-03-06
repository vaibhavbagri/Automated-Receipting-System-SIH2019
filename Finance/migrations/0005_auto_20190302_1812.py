# Generated by Django 2.0 on 2019-03-02 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0004_auto_20190302_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(default='templates/assets/images/company/logo-text.png', upload_to='templates/assets/images/company')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Finance.Company'),
        ),
        migrations.AddField(
            model_name='items',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Finance.Company'),
        ),
        migrations.AddField(
            model_name='receiptdata',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Finance.Company'),
        ),
        migrations.AddField(
            model_name='uploads',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Finance.Company'),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Finance.Company'),
        ),
    ]
