# Generated by Django 4.0.6 on 2022-08-16 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_relationship_article_alter_relationship_scope'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='scopes',
        ),
        migrations.AddField(
            model_name='scope',
            name='scopes1',
            field=models.ManyToManyField(related_name='scopes1', through='articles.Relationship', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.scope', verbose_name='Раздел'),
        ),
    ]
