# Generated by Django 3.2.4 on 2023-02-07 16:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20230205_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorConnectDB',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Content', models.CharField(max_length=2000)),
                ('updated_date', models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 271316, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 271316, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='awards',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 265703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='awards',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 265703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='birac',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 271316, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 271316, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carrer',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 271316, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 265703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 265703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventsform',
            name='company',
            field=models.CharField(default='company', max_length=200),
        ),
        migrations.AlterField(
            model_name='eventsform',
            name='event',
            field=models.CharField(default='event', max_length=200),
        ),
        migrations.AlterField(
            model_name='eventsform',
            name='image',
            field=models.ImageField(default='carrer/Screenshot_3.png', upload_to='EventsForm/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='eventsform',
            name='linkedin',
            field=models.CharField(default='linkedin', max_length=200),
        ),
        migrations.AlterField(
            model_name='eventsform',
            name='title',
            field=models.CharField(default='title', max_length=200),
        ),
        migrations.AlterField(
            model_name='eventsform',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 271316, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventsform',
            name='website',
            field=models.CharField(default='website', max_length=200),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 265703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='latest_news',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 271316, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logo',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 265703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mission',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 270806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sisfs',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 271316, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tbi',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 271316, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 265703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 265703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='value',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 270806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vision',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 16, 47, 32, 265703, tzinfo=utc)),
        ),
    ]