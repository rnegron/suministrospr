# Generated by Django 2.2.9 on 2020-01-18 18:47

import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
from django.db import migrations, models, transaction

import suministrospr.utils.fields

from ..constants import MUNICIPALITIES


def create_municipalities(apps, schema_editor):
    Municipality = apps.get_model("suministros", "Municipality")

    for muncipality_name in MUNICIPALITIES.values():
        Municipality.objects.create(name=muncipality_name)


def copy_municipality_data_to_new_column(apps, schema_editor):
    Suministro = apps.get_model("suministros", "Suministro")
    Municipality = apps.get_model("suministros", "Municipality")

    municipality_slug_to_instance_map = dict()

    all_municipalities = Municipality.objects.all()
    for municipality in all_municipalities:
        municipality_slug_to_instance_map[municipality.slug] = municipality

    suministros = Suministro.objects.select_for_update().all()

    with transaction.atomic():
        for suministro in suministros:
            suministro.municipality_fk = municipality_slug_to_instance_map[
                suministro.municipality
            ]
            suministro.save()


class Migration(migrations.Migration):

    replaces = [
        ("suministros", "0001_initial"),
        ("suministros", "0002_auto_20200113_2247"),
        ("suministros", "0003_auto_20200113_2325"),
        ("suministros", "0004_suministro_slug"),
        ("suministros", "0005_auto_20200115_2301"),
        ("suministros", "0006_auto_20200117_1500"),
        ("suministros", "0007_auto_20200117_2309"),
        ("suministros", "0008_auto_20200117_2312"),
        ("suministros", "0009_auto_20200117_2313"),
        ("suministros", "0010_suministro_municipality_fk"),
        ("suministros", "0011_auto_20200117_2315"),
        ("suministros", "0012_remove_suministro_municipality"),
        ("suministros", "0013_auto_20200117_2316"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    suministrospr.utils.fields.DateTimeCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified_at",
                    suministrospr.utils.fields.DateTimeModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        max_length=255,
                        populate_from=["name"],
                    ),
                ),
            ],
            options={
                "ordering": ("-modified_at", "-created_at"),
                "get_latest_by": "modified_at",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Suministro",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    suministrospr.utils.fields.DateTimeCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified_at",
                    suministrospr.utils.fields.DateTimeModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "municipality",
                    models.CharField(
                        choices=[
                            ("adjuntas", "Adjuntas"),
                            ("aguada", "Aguada"),
                            ("aguadilla", "Aguadilla"),
                            ("aguas-buenas", "Aguas Buenas"),
                            ("aibonito", "Aibonito"),
                            ("anasco", "Añasco"),
                            ("arecibo", "Arecibo"),
                            ("arroyo", "Arroyo"),
                            ("barceloneta", "Barceloneta"),
                            ("barranquitas", "Barranquitas"),
                            ("bayamon", "Bayamón"),
                            ("cabo-rojo", "Cabo Rojo"),
                            ("caguas", "Caguas"),
                            ("camuy", "Camuy"),
                            ("canovanas", "Canóvanas"),
                            ("carolina", "Carolina"),
                            ("catano", "Catano"),
                            ("cayey", "Cayey"),
                            ("ceiba", "Ceiba"),
                            ("ciales", "Ciales"),
                            ("cidra", "Cidra"),
                            ("coamo", "Coamo"),
                            ("comerio", "Comerío"),
                            ("corozal", "Corozal"),
                            ("culebra", "Culebra"),
                            ("dorado", "Dorado"),
                            ("fajardo", "Fajardo"),
                            ("florida", "Florida"),
                            ("guanica", "Guánica"),
                            ("guayama", "Guayama"),
                            ("guayanilla", "Guayanilla"),
                            ("guaynabo", "Guaynabo"),
                            ("gurabo", "Gurabo"),
                            ("hatillo", "Hatillo"),
                            ("hormigueros", "Hormigueros"),
                            ("humacao", "Humacao"),
                            ("isabela", "Isabela"),
                            ("jayuya", "Jayuya"),
                            ("juana-diaz", "Juana Díaz"),
                            ("juncos", "Juncos"),
                            ("lajas", "Lajas"),
                            ("lares", "Lares"),
                            ("las-marias", "Las Marías"),
                            ("las-piedras", "Las Piedras"),
                            ("loiza", "Loiza"),
                            ("luquillo", "Luquillo"),
                            ("manati", "Manatí"),
                            ("maricao", "Maricao"),
                            ("maunabo", "Maunabo"),
                            ("mayaguez", "Mayagüez"),
                            ("moca", "Moca"),
                            ("morovis", "Morovis"),
                            ("naguabo", "Naguabo"),
                            ("naranjito", "Naranjito"),
                            ("orocovis", "Orocovis"),
                            ("patillas", "Patillas"),
                            ("penuelas", "Peñuelas"),
                            ("ponce", "Ponce"),
                            ("quebradillas", "Quebradillas"),
                            ("rincon", "Rincón"),
                            ("rio-grande", "Río Grande"),
                            ("sabana-grande", "Sabana Grande"),
                            ("salinas", "Salinas"),
                            ("san-german", "San Germán"),
                            ("san-juan", "San Juan"),
                            ("san-lorenzo", "San Lorenzo"),
                            ("san-sebastian", "San Sebastián"),
                            ("santa-isabel", "Santa Isabel"),
                            ("toa-alta", "Toa Alta"),
                            ("toa-baja", "Toa Baja"),
                            ("trujillo-alto", "Trujillo Alto"),
                            ("utuado", "Utuado"),
                            ("vega-alta", "Vega Alta"),
                            ("vega-baja", "Vega Baja"),
                            ("vieques", "Vieques"),
                            ("villalba", "Villalba"),
                            ("yabucoa", "Yabucoa"),
                            ("yauco", "Yauco"),
                        ],
                        max_length=255,
                    ),
                ),
                ("content", ckeditor.fields.RichTextField()),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        max_length=255,
                        populate_from=["title", "municipality"],
                    ),
                ),
                ("tags", models.ManyToManyField(blank=True, to="suministros.Tag")),
            ],
            options={
                "ordering": ("-modified_at", "-created_at"),
                "get_latest_by": "modified_at",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Municipality",
            fields=[
                (
                    "created_at",
                    suministrospr.utils.fields.DateTimeCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified_at",
                    suministrospr.utils.fields.DateTimeModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("adjuntas", "Adjuntas"),
                            ("aguada", "Aguada"),
                            ("aguadilla", "Aguadilla"),
                            ("aguas-buenas", "Aguas Buenas"),
                            ("aibonito", "Aibonito"),
                            ("anasco", "Añasco"),
                            ("arecibo", "Arecibo"),
                            ("arroyo", "Arroyo"),
                            ("barceloneta", "Barceloneta"),
                            ("barranquitas", "Barranquitas"),
                            ("bayamon", "Bayamón"),
                            ("cabo-rojo", "Cabo Rojo"),
                            ("caguas", "Caguas"),
                            ("camuy", "Camuy"),
                            ("canovanas", "Canóvanas"),
                            ("carolina", "Carolina"),
                            ("catano", "Catano"),
                            ("cayey", "Cayey"),
                            ("ceiba", "Ceiba"),
                            ("ciales", "Ciales"),
                            ("cidra", "Cidra"),
                            ("coamo", "Coamo"),
                            ("comerio", "Comerío"),
                            ("corozal", "Corozal"),
                            ("culebra", "Culebra"),
                            ("dorado", "Dorado"),
                            ("fajardo", "Fajardo"),
                            ("florida", "Florida"),
                            ("guanica", "Guánica"),
                            ("guayama", "Guayama"),
                            ("guayanilla", "Guayanilla"),
                            ("guaynabo", "Guaynabo"),
                            ("gurabo", "Gurabo"),
                            ("hatillo", "Hatillo"),
                            ("hormigueros", "Hormigueros"),
                            ("humacao", "Humacao"),
                            ("isabela", "Isabela"),
                            ("jayuya", "Jayuya"),
                            ("juana-diaz", "Juana Díaz"),
                            ("juncos", "Juncos"),
                            ("lajas", "Lajas"),
                            ("lares", "Lares"),
                            ("las-marias", "Las Marías"),
                            ("las-piedras", "Las Piedras"),
                            ("loiza", "Loiza"),
                            ("luquillo", "Luquillo"),
                            ("manati", "Manatí"),
                            ("maricao", "Maricao"),
                            ("maunabo", "Maunabo"),
                            ("mayaguez", "Mayagüez"),
                            ("moca", "Moca"),
                            ("morovis", "Morovis"),
                            ("naguabo", "Naguabo"),
                            ("naranjito", "Naranjito"),
                            ("orocovis", "Orocovis"),
                            ("patillas", "Patillas"),
                            ("penuelas", "Peñuelas"),
                            ("ponce", "Ponce"),
                            ("quebradillas", "Quebradillas"),
                            ("rincon", "Rincón"),
                            ("rio-grande", "Río Grande"),
                            ("sabana-grande", "Sabana Grande"),
                            ("salinas", "Salinas"),
                            ("san-german", "San Germán"),
                            ("san-juan", "San Juan"),
                            ("san-lorenzo", "San Lorenzo"),
                            ("san-sebastian", "San Sebastián"),
                            ("santa-isabel", "Santa Isabel"),
                            ("toa-alta", "Toa Alta"),
                            ("toa-baja", "Toa Baja"),
                            ("trujillo-alto", "Trujillo Alto"),
                            ("utuado", "Utuado"),
                            ("vega-alta", "Vega Alta"),
                            ("vega-baja", "Vega Baja"),
                            ("vieques", "Vieques"),
                            ("villalba", "Villalba"),
                            ("yabucoa", "Yabucoa"),
                            ("yauco", "Yauco"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        max_length=255,
                        populate_from=["name"],
                    ),
                ),
            ],
            options={
                "verbose_name": "municipality",
                "verbose_name_plural": "municipalities",
            },
        ),
        migrations.AlterModelOptions(
            name="suministro",
            options={
                "verbose_name": "suministro",
                "verbose_name_plural": "suministros",
            },
        ),
        migrations.AddIndex(
            model_name="suministro",
            index=models.Index(fields=["title"], name="suministros_title_dfc01c_idx"),
        ),
        migrations.RunPython(create_municipalities),
        migrations.AddField(
            model_name="suministro",
            name="municipality_fk",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="suministros",
                related_query_name="suministro",
                to="suministros.Municipality",
            ),
        ),
        migrations.RunPython(copy_municipality_data_to_new_column),
        migrations.RemoveField(model_name="suministro", name="municipality",),
        migrations.RenameField(
            model_name="suministro",
            old_name="municipality_fk",
            new_name="municipality",
        ),
    ]
