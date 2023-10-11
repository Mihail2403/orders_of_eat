from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView
from rest_framework import generics

from .pagination import OrderListPagination

from .serializer import EatItemSerializer, WorkerSerializer
from .models import EatItem, EatOfOrder, Order, Worker


# список сотрудников
class WorkerListAPIView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

# список блюд
class EatItemListAPIView(generics.ListAPIView):
    queryset = EatItem.objects.all()
    serializer_class = EatItemSerializer

# добавление заказа
class OrderAPIView(APIView):
    def post(self, request):
        try:
            dateOrder = date.fromordinal(request.data["date"])
            worker = Worker.objects.get(id=request.data["worker_id"])
            order = Order.objects.create(date=dateOrder, worker=worker)
            for eat in request.data["eats"]:
                EatOfOrder.objects.create(
                    eatItem=EatItem(id=eat['eat']['id']),
                    order=order
                    )
            return response.Response({"status":"good","order":{"id":order.id, "worker": order.worker.name}})
        except Exception as e:
            print(e)
            return response.Response({"status": "bad"})


# история заказов
class HistoryOfOrdersAPIView(APIView):
    def get(self, request):
        try:
            orders = []
            # тк order - foreign key для EatOfOrder -> чтобы сгенерить ответ, проходим процедуру сбора всех EatOfOrder-ов
            for order in Order.objects.all():
                eatList = []
                eatObjectsList = []
                for eatOfOrder in EatOfOrder.objects.filter(order=order):
                    if not next(filter(lambda obj: obj.eatItem==eatOfOrder.eatItem, eatList), None):
                        eatObjectsList.append(
                            # объект eatItem, подходящий для сериализации
                                {
                                    "id": eatOfOrder.id, 
                                    "eat": {
                                        "id":eatOfOrder.eatItem.id,
                                        "text":eatOfOrder.eatItem.name,
                                        "components":eatOfOrder.eatItem.components,
                                        "price":eatOfOrder.eatItem.price
                                    },
                                    "count": 1
                                    }
                            )
                        eatList.append(eatOfOrder)
                    else:
                        next(
                                filter(lambda obj: obj["eat"]["id"] == eatOfOrder.eatItem.id, eatObjectsList),
                                None
                            )["count"]+=1
                order_object = {
                    "id": order.id,
                    "date": order.date.toordinal(),
                    "person":{
                        "id":order.worker.id, 
                        "name":order.worker.name
                        },
                    "Eats": eatObjectsList
                }
                orders.append(order_object)
            return response.Response({"status":"good", "order_list":orders})
        except Exception as e:
            print(e)
            return response.Response({"status":"bad"})
        
