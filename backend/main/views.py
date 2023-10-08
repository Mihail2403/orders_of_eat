from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView
from rest_framework import generics

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
                    eatItem=EatItem(id=eat["id"]),
                    order=order
                    )
            return response.Response({"status":"good","order":order.id})
        except Exception as e:
            print(e)
            return response.Response({"status": "bad"})

# история заказов 
class HistoryOfOrdersAPIView(APIView):
    def get(self, request):
        try:
            orders = []
            for order in Order.objects.all():
                eatList = []
                eatObjectsList = []
                for eatOfOrder in EatOfOrder.objects.filter(order=order):
                    if eatOfOrder not in eatList:
                        eatObjectsList.append({"eat":eatOfOrder, "count":1})
                        eatList.append(eatOfOrder)
                    else:
                        pass

            return response.Response({"status":"good"})
        except Exception as e:
            print(e)
            return response.Response({"status":"bad"})