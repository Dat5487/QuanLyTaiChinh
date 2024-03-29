# Generated by Django 4.2.8 on 2024-01-25 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("ThongTin", "0001_initial"),
        ("DanhMucThuChi", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="KeHoachThu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dotThu", models.IntegerField()),
                ("trangThai", models.BooleanField(blank=True, null=True)),
                ("soTien", models.BigIntegerField()),
                ("ngayBatDau", models.DateField(blank=True, null=True)),
                ("ngayKetThuc", models.DateField(blank=True, null=True)),
                ("noiDung", models.TextField()),
                (
                    "khoaHoc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ChuongTrinhHoc.khoahoc",
                    ),
                ),
                (
                    "khoanThu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="DanhMucThuChi.danhmucthuchi",
                    ),
                ),
                (
                    "nganhDaoTao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ChuongTrinhHoc.nganhdaotao",
                    ),
                ),
            ],
        ),
    ]
