from django.db import models



class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    
    class Meta:
        # Уникальность по имени и типу
        unique_together = ('name', 'type')
    
    def __str__(self):
        return f"{self.name} ({self.type})"


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        # Уникальность по имени и категории
        unique_together = ('name', 'category')
    
    def __str__(self):
        return f"{self.name} ({self.category})"


class DDSRecord(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()  # Дата, которую можно редактировать
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()  # Сумма в рублях
    comment = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.date} - {self.amount}р"