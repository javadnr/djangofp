from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Items,Review
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class ItemlistView(LoginRequiredMixin, ListView):
    model = Items
    template_name = 'items/item.html'
    context_object_name = 'item_list'
    login_url = 'account_login'

class ItemdetailView(LoginRequiredMixin, DetailView):
    model = Items
    template_name = 'items/detail.html'
    context_object_name = "item_detail"
    login_url = 'account_login'

class CreateView(LoginRequiredMixin, CreateView):
    model = Items
    template_name = 'items/create_item.html'
    fields = "__all__"

class AddreviewView(CreateView):
    model = Review
    template_name = 'items/review.html'
    fields = '__all__'