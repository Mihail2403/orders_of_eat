from rest_framework import serializers

from .models import Worker, EatItem

# сериализатор списка сотрудников
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


# сериализатор списка блюд, возможных к заказу 
class EatItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EatItem
        fields = '__all__'