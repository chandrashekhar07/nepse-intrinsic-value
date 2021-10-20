from django.urls import path
from .views import StockListView,StockCreateView, StockUpdateView, StockDeleteView

app_name = 'stockapp'
urlpatterns = [
    path('', StockListView.as_view(),name='list'),
    path('create/',StockCreateView.as_view(),name='create'),
    path('<int:id>/update/',StockUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',StockDeleteView.as_view(),name='delete'),

]