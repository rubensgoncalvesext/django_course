from django.urls import path
from .views import primeira_view, template1

urlpatterns = [
	path('', primeira_view, name='first_view'),
	path('jose/', template1, name='second_view'),
]