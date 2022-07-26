# Generated by Django 2.2.9 on 2022-07-24 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20220626_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='descricao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='card_descricao_elemento', to='api.ElementoComunicativo'),
        ),
        migrations.AlterField(
            model_name='card',
            name='titulo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='card_titulo_elemento', to='api.ElementoComunicativo'),
        ),
        migrations.AlterField(
            model_name='preceptor',
            name='avatar',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roteiro',
            name='descricao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='roteiro_descricao_elemento', to='api.ElementoComunicativo'),
        ),
        migrations.AlterField(
            model_name='roteiro',
            name='titulo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='roteiro_titulo_elemento', to='api.ElementoComunicativo'),
        ),
    ]
