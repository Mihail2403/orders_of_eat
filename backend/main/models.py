from django.db import models


# сотрудники, на имена которых будут заказывать еду
class Worker(models.Model):
    name = models.CharField(max_length=80)
    
    def __str__(self) -> str:
        return self.name
    
# блюда, возможные к заказу
class EatItem(models.Model):
    name = models.CharField(max_length=30)
    # состав блюда
    components = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} - {self.price} руб."

# заказ
class Order(models.Model):
    date = models.DateField()
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.worker} c id={self.id}"

# блюдо заказа
class EatOfOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    eatItem = models.ForeignKey(EatItem, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.eatItem.name} - {self.order.date}({self.order.worker})"