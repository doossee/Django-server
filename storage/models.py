from django.db import models


class Product(models.Model):

    """Товар"""

    class TypeChoices(models.TextChoices):
        DIAPER = "Diaper", "Памперс"
        SOAP = "Soap", "Мыло"
        WIPES = "Wipes", "Влажные салфетки"

    name = models.CharField("Название товара", max_length=150)
    type = models.CharField("Тип товара", max_length=6, choices=TypeChoices.choices)
    balance = models.DecimalField("Остаток товара", max_digits=9, decimal_places=2)

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
    
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, verbose_name="Товар"
        )
    amount = models.PositiveSmallIntegerField("Количество товара")
    date_of = models.DateField("Дата прихода", auto_now_add=True)

    def save(self):
        if not self.id:
            temp = self.product
            temp.balance += self.amount
            temp.save()
        super(Advent, self).save()

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = "Приход"
        verbose_name_plural = "Приходы"


class Consumption(models.Model):
    
    """Расход"""

    client = models.ForeignKey(
        Client, on_delete=models.PROTECT, verbose_name="Клиент"
        )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, verbose_name="Товар"
    )
    price = models.DecimalField("Цена товара", max_digits=9, decimal_places=2)
    amount = models.PositiveSmallIntegerField("Количество товара")
    sum = models.DecimalField("Общая сумма", max_digits=9, decimal_places=2, editable=False)
    date_of = models.DateField("Дата расхода", auto_now_add=True)

    def save(self):
        if not self.id:
            temp = self.product
            if temp.balance >= self.amount > 0 :
                self.sum = self.price * self.amount
                temp.balance -= self.amount
                temp.save()
                self.client.debt += self.sum
                self.client.save()
        super(Consumption, self).save()

    def __str__(self):
        return f"{self.client} - {self.product}"
    
    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"

    
class Profit(models.Model):
    
    """Прибыль"""

    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name="Клиент")
    sum_of_profit = models.DecimalField("Сумма прибыли", max_digits=9, decimal_places=2)
    date_of = models.DateField("Дата прибыли", auto_now_add=True)

    def save(self):
        if not self.id:
            self.client.debt -= self.sum_of_minus
            self.client.save()
        super(Profit, self).save()

    def __str__(self):
        return f"{self.client}"

    class Meta:
        verbose_name = "Прибыль"
        verbose_name_plural = "Прибыли"

