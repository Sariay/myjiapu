from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class MigrationRoadsView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        return render(request, 'migrationRoads.html')


class LineageTreeView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        return render(request, 'lineageTree.html')


class GravesMapView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        return render(request, 'gravesMap.html')