from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 32, verbose_name = ' 상품명')
    price = models.IntegerField(verbose_name = '가격')
    description = models.TextField(verbose_name = '상세설명')
    stock = models.IntegerField(verbose_name = '수량')
    register_date = models.DateTimeField(auto_now_add = True, verbose_name = '등록날짜')

    def __str__(self):
        return self.name

    class Meta :
        db_table = 'product_talbe'
        verbose_name = '상품'
        verbose_name_plural = '상품들'

