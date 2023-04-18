from django.db import models


class Product(models.Model):

    """Товар"""

    class TypeChoices(models.TextChoices):
        DIAPER = "Diaper", "Памперс"
        SOAP = "Soap", "Мыло"
        WIPES = "Wipes", "Влажные салфетки"

    name = models.CharField("Название товара", max_length=150)
    type = models.CharField("Тип товара", max_length=6, choices=TypeChoices.choices)
    balance = models.PositiveIntegerField("Количество товара", default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Client(models.Model):

    """Клиент"""

    name = models.CharField("Имя клиента", max_length=60)
    description = models.CharField("Описание", max_length=100)
    phone_number = models.CharField("Телефонный номер", max_length=13)
    debt = models.DecimalField("Долг", max_digits=9, decimal_places=2, default="0")
    status = models.BooleanField("Статус Клиента", default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class SingleAdvent(models.Model):

    """Приход"""
    
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING, 
        verbose_name="Товар"
    )
    amount = models.PositiveIntegerField("Количество товара")

    def __str__(self):
        return f"{self.product}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.product.balance += self.amount
            self.product.save()
        super(SingleAdvent, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Приход"
        verbose_name_plural = "Приходы"


class AdventList(models.Model):

    """Список приходов"""

    advent = models.ManyToManyField(SingleAdvent, verbose_name="Приход")
    created_at = models.DateField("Дата прихода", auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return f"{self.created_at}"
    
    class Meta:
        verbose_name = "Список приходов"
        verbose_name_plural = "Списки приходов"


class SingleConsumption(models.Model):
    
    """Расход"""

    product = models.ForeignKey(
        Product, 
        on_delete=models.DO_NOTHING, 
        verbose_name="Товар"
    )
    amount = models.PositiveIntegerField("Количество товара")
    price = models.DecimalField("Цена товара", max_digits=9, decimal_places=2)
    cost = models.DecimalField("Стоимость", max_digits=9, decimal_places=2, editable=False)

    def __str__(self):
        return f"{self.product}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.cost = self.amount * self.price
            if self.product.balance >= self.amount:
                self.product.balance -= self.amount
                self.product.save()
        super(SingleConsumption, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"


class ConsumptionList(models.Model):

    """Список расходов"""

    client = models.ForeignKey(
        Client,
        on_delete=models.DO_NOTHING,
        verbose_name="Клиент"
    )
    consumption = models.ManyToManyField(
        SingleConsumption,
        verbose_name="Расход"
    )
    total_cost = models.DecimalField("Общая стоимость", max_digits=9, decimal_places=2, default=0)
    created_at = models.DateField("Дата расхода", auto_now_add=True)

    def __str__(self):
        return f"{self.client}-{self.total_cost}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.client.debt += self.total_cost
            self.client.save()
        super(ConsumptionList, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Список расходов"
        verbose_name_plural = "Списки расходов"

    
class Profit(models.Model):
    
    """Прибыль"""

    client = models.ForeignKey(
        Client, 
        on_delete=models.DO_NOTHING, 
        verbose_name="Клиент"
    )
    profit = models.DecimalField("Сумма прибыли", max_digits=9, decimal_places=2)
    created_at = models.DateField("Дата прибыли", auto_now_add=True)

    def __str__(self):
        return f"{self.client}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.client.debt -= self.profit
            self.client.save()
        super(Profit, self).save(*args,**kwargs)

    class Meta:
        verbose_name = "Прибыль"
        verbose_name_plural = "Прибыли"

