# Generated by Django 5.1.7 on 2025-04-10 13:28

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateField(auto_now_add=True)),
                ('updated_ed', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('descriptions', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateField(auto_now_add=True)),
                ('updated_ed', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('descriptions', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateField(auto_now_add=True)),
                ('updated_ed', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('descriptions', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateField(auto_now_add=True)),
                ('updated_ed', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('descriptions', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateField(auto_now_add=True)),
                ('updated_ed', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateField(auto_now_add=True)),
                ('updated_ed', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('descriptions', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_ed', models.DateField(auto_now_add=True)),
                ('updated_ed', models.DateField(auto_now=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message="Telefon raqam '+998XXXXXXXXX' formatida bo'lishi kerak!", regex='^\\+998\\d{9}$')])),
                ('is_admin', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_student', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateField(auto_now_add=True)),
                ('updated_ed', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('descriptions', models.CharField(blank=True, max_length=500, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user_auth.course')),
                ('table', models.ManyToManyField(to='user_auth.table')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateField(auto_now_add=True)),
                ('updated_ed', models.DateField(auto_now=True)),
                ('is_line', models.BooleanField(default=False)),
                ('descriptions', models.CharField(blank=True, max_length=500, null=True)),
                ('group', models.ManyToManyField(related_name='get_group', to='user_auth.groupstudent')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateField(auto_now_add=True)),
                ('updated_ed', models.DateField(auto_now=True)),
                ('full_name', models.CharField(blank=True, max_length=150, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True)),
                ('addres', models.CharField(blank=True, max_length=150, null=True)),
                ('descriptions', models.CharField(blank=True, max_length=500, null=True)),
                ('student', models.ManyToManyField(related_name='student', to='user_auth.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateField(auto_now_add=True)),
                ('updated_ed', models.DateField(auto_now=True)),
                ('descriptions', models.CharField(blank=True, max_length=500, null=True)),
                ('course', models.ManyToManyField(related_name='get_course', to='user_auth.course')),
                ('departments', models.ManyToManyField(related_name='get_department', to='user_auth.departments')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='groupstudent',
            name='teacher',
            field=models.ManyToManyField(to='user_auth.teacher'),
        ),
    ]
