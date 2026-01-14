from django.urls import path
from .views import map_view, field_data, fields_geojson, field_details

urlpatterns = [
    path("", map_view, name="dashboard_map"),
    path("fields/", fields_geojson, name="fields_geojson"),

    # IMPORTANT: string field number
    path("field-details/<str:field_no>/", field_details, name="field_details"),

    # optional legacy/demo
    path("field/<int:field_id>/", field_data, name="field_data"),
]
