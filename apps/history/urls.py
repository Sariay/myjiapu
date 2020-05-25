from django.conf.urls import url
from django.urls import path

from . import views
from apps.history.views import MigrationRoadsView, LineageTreeView, GravesMapView

urlpatterns = [
    url(r'^migrationRoads/$', MigrationRoadsView.as_view(), name="migrationRoads"),
    url(r'^lineageTree/$', LineageTreeView.as_view(), name="lineageTree"),
    url(r'^gravesMap/$', GravesMapView.as_view(), name="gravesMap"),
]