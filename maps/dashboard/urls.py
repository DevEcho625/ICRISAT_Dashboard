from django.urls import path
from .views import map_view, field_data

urlpatterns = [
    path("", map_view, name="dashboard_map"),
    path("field/<int:field_id>/", field_data, name="field_data"),
]
