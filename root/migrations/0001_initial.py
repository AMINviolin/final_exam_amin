# Generated by Django 4.2.5 on 2023-10-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('properties', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='team.png', upload_to='team')),
                ('firstname', models.CharField(max_length=40)),
                ('twitter', models.CharField(default='twitter.com', max_length=255)),
                ('facebook', models.CharField(default='facebook.com', max_length=255)),
                ('instagram', models.CharField(default='instagram.com', max_length=255)),
                ('linkedin', models.CharField(default='linkedin.com', max_length=255)),
                ('category', models.ManyToManyField(to='root.category')),
            ],
        ),
        migrations.CreateModel(
            name='PortFolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='portfolio')),
                ('title', models.CharField(max_length=40)),
                ('ouner_name', models.CharField(default='ouner', max_length=60)),
                ('content1', models.TextField(default='.....', max_length=10000)),
                ('content2', models.TextField(blank=True, default='.....', max_length=2000, null=True)),
                ('ouner_image', models.ImageField(default='default.jpg', upload_to='portfolio')),
                ('description', models.TextField()),
                ('client', models.TextField()),
                ('project_date', models.DateTimeField(auto_now_add=True)),
                ('project_url', models.URLField(blank=True, null=True)),
                ('subject', models.CharField(default='bigan', max_length=250)),
                ('status', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(related_name='portfolio_category', to='root.category')),
                ('ouner_category', models.ManyToManyField(related_name='portfolio_owner_category', to='root.category')),
            ],
        ),
    ]
