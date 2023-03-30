from django.urls import path
from .views import SchoolCreateView, SchoolListView

urlpatterns = [
    path('schools/', SchoolCreateView.as_view(), name='create_school'),
    path('schools/list/', SchoolListView.as_view(), name='list_schools'),
]
