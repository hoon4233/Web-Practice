from django.db import models

class Order(models.Model):
    user = models.ForeignKey('users.Users', verbose_name = '사용자', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', verbose_name = '상품명', on_delete=models.CASCADE)
    register_date = models.DateTimeField(auto_now_add=True, verbose_name = '등록날짜')
    quantity = models.IntegerField(verbose_name = '수량')

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)

    class Meta :
        db_table = 'order_table' 
        verbose_name = '주문'
        verbose_name_plural = '주문들'
