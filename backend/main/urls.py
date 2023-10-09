from django.urls import path

from .views import EatItemListAPIView, OrderAPIView, WorkerListAPIView, HistoryOfOrdersAPIView

urlpatterns = [
    path('worker-list/', WorkerListAPIView.as_view()),
    path('eat-list/', EatItemListAPIView.as_view()),
    path('order/', OrderAPIView.as_view()),
    path('history/', HistoryOfOrdersAPIView.as_view())
]
