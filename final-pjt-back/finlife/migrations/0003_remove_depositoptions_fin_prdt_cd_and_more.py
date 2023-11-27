from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finlife', '0002_depositoptions_fin_prdt_cd_savingoptions_fin_prdt_cd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depositoptions',
            name='fin_prdt_cd',
        ),
        migrations.RemoveField(
            model_name='savingoptions',
            name='fin_prdt_cd',
        ),
    ]
