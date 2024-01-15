# Generated by Django 4.2.9 on 2024-01-15 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='event',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_holder',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
