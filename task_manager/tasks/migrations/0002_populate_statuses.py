from django.db import migrations

def populate_statuses(apps, schema_editor):
    Status = apps.get_model('tasks', 'Status')
    statuses = [
        "To-do",
        "In-progress",
        "Completed",
    ]
    for status_name in statuses:
        Status.objects.create(name=status_name)

class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_statuses),
    ]
