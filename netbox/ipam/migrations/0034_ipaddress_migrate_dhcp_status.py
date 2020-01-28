from django.db import migrations, models


def ipaddress_status_to_slug(apps, schema_editor):
    IPAddress = apps.get_model('ipam', 'IPAddress')
    IPAddress.objects.filter(status='5').update(status='dhcp')


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('ipam', '0033_deterministic_ordering'),
    ]

    operations = [

        # IPAddress.status
        migrations.RunPython(
            code=ipaddress_status_to_slug
        ),

    ]
