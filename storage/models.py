from django.db import models


class Product(models.Model):

    """Товар"""

    class TypeChoices(models.TextChoices):
        DIAPER = "Diaper", "Памперс"
        SOAP = "Soap", "Мыло"
        WIPES = "Wipes", "Влажные салфетки"

    name = models.CharField("Название товара", max_length=150)
    type = models.CharField("Тип товара", max_length=6, choices=TypeChoices.choices)
    balance = models.PositiveIntegerField("Остаток товара")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Client(models.Model):

    """Клиент"""

    name = models.CharField("Имя клиента", max_length=60)
    status = models.BooleanField("Статус Клиента", default=True)
    description = models.CharField("Описание", max_length=100)
    phone_number = models.CharField("Телефонный номер", max_length=13)
    debt = models.DecimalField("Долг", max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Advent(models.Model):

    """Приход"""
    
    products = models.ForeignKey(
        Product, 
        on_delete=models.PROTECT, 
        verbose_name="Товар"
        )
    amount = models.PositiveIntegerField("Количество товара")
    date_of = models.DateField("Дата прихода", auto_now_add=True)

    def __str__(self):
        return f"{self.products}"

    class Meta:
        verbose_name = "Приход"
        verbose_name_plural = "Приходы"


class Consumption(models.Model):
    
    """Расход"""

    client = models.ForeignKey(
        Client, 
        related_name='client', 
        on_delete=models.PROTECT, 
        verbose_name="Клиент"
        )
    products = models.ForeignKey(
        Product, 
        related_name='products', 
        on_delete=models.PROTECT, 
        verbose_name="Продукты"
    )
    price = models.DecimalField("Цена товара", max_digits=9, decimal_places=2)
    amount = models.PositiveIntegerField("Количество товара")
    sum = models.DecimalField("Общая сумма", max_digits=9, decimal_places=2, editable=False)
    date_of = models.DateField("Дата расхода", auto_now_add=True)

    def __str__(self):
        return f"{self.client} - {self.products}"
    
    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"

    
class Profit(models.Model):
    
    """Прибыль"""

    client = models.ForeignKey(
        Client, 
        on_delete=models.PROTECT, 
        verbose_name="Клиент"
    )
    sum_of_profit = models.DecimalField("Сумма прибыли", max_digits=9, decimal_places=2)
    date_of = models.DateField("Дата прибыли", auto_now_add=True)

    def __str__(self):
        return f"{self.client}"

    class Meta:
        verbose_name = "Прибыль"
        verbose_name_plural = "Прибыли"

