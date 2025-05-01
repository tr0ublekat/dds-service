from django.db import models



class Status(models.Model):
    name = models.CharField("Статус", max_length=100, unique=True)

    class Meta:
        verbose_name = "Статус"          # Название в единственном числе
        verbose_name_plural = "Статусы"  # Название во множественном числе

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField("Тип", max_length=100, unique=True)

    class Meta:
        verbose_name = "Тип"          # Название в единственном числе
        verbose_name_plural = "Типы"  # Название во множественном числе
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Категория", max_length=100)
    type = models.ForeignKey(Type, verbose_name="Тип", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Категория"          # Название в единственном числе
        verbose_name_plural = "Категории"  # Название во множественном числе

    def __str__(self):
        return f"{self.name} ({self.type})"


class Subcategory(models.Model):
    name = models.CharField("Подкатегория", max_length=100)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Подкатегория"          # Название в единственном числе
        verbose_name_plural = "Подкатегории"  # Название во множественном числе

    def __str__(self):
        return f"{self.name} ({self.category})"


# Основная модель ДДС
class DDSEntry(models.Model):
    date = models.DateField("Дата записи")
    status = models.ForeignKey(Status, verbose_name="Статус", on_delete=models.PROTECT)
    type = models.ForeignKey(Type, verbose_name="Тип", on_delete=models.PROTECT)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, verbose_name="Подкатегория", on_delete=models.PROTECT)
    amount = models.DecimalField("Сумма (руб)", max_digits=12, decimal_places=2)
    comment = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Движение денежных средств"          # Название в единственном числе
        verbose_name_plural = "Движения денежных средств"  # Название во множественном числе

    def __str__(self):
        return f"{self.date} | {self.type} | {self.amount} руб"