from django.urls import path
from .views import ItemlistView, ItemdetailView, CreateView,AddreviewView
urlpatterns = [
    path('',ItemlistView.as_view(), name='item'),
    path('<uuid:pk>',ItemdetailView.as_view(),name = "item_detail"),
    path('newitem/',CreateView.as_view(), name= 'new_item'),
    path('review/',AddreviewView.as_view(),name='review'),
]
