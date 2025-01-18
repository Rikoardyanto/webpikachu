from django.db import models

class Produk(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='produk_gambar/')
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.PositiveIntegerField()

    def __str__(self):
        return self.nama