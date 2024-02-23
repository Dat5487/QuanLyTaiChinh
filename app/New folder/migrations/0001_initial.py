# Generated by Django 4.2.8 on 2024-01-25 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HeDaoTao",
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
                ("tenHeDaoTao", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Khoa",
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
                ("tenKhoa", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="KhoaHoc",
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
                ("namKhoaHoc", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="NamHoc",
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
                ("namHoc", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="NganhDaoTao",
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
                ("tenNganhDaoTao", models.CharField(max_length=100)),
                (
                    "heDaoTao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.hedaotao",
                    ),
                ),
                (
                    "khoa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.khoa",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lop",
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
                ("lop", models.CharField(max_length=100)),
                (
                    "heDaoTao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.hedaotao",
                    ),
                ),
                (
                    "khoa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.khoa",
                    ),
                ),
                (
                    "khoaHoc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.khoahoc",
                    ),
                ),
                (
                    "nganhDaoTao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.nganhdaotao",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SinhVien",
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
                ("maSV", models.CharField(max_length=10)),
                ("hoTen", models.CharField(max_length=100)),
                ("ngaySinh", models.DateField(blank=True, null=True)),
                ("queQuan", models.CharField(max_length=100)),
                ("trangThai", models.BooleanField(blank=True)),
                (
                    "lop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.lop",
                    ),
                ),
            ],
        ),
    ]