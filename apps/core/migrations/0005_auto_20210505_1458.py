# Generated by Django 3.2 on 2021-05-05 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210505_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='autorecomendacii',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Код авторекомендации'),
        ),
        migrations.AddField(
            model_name='autorecomendacii',
            name='use',
            field=models.BooleanField(default=False, verbose_name='Использовать'),
        ),
        migrations.AlterField(
            model_name='novorojdenniy',
            name='pol_novorojdennogo',
            field=models.IntegerField(blank=True, choices=[(1, 'М'), (2, 'Ж'), (3, 'Неизвестен'), (4, 'Интерсекс')], null=True, verbose_name='Пол новорожденного'),
        ),
    ]
