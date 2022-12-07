from django.urls import path
from Adoration import views
urlpatterns = [
    path('',views.Main,name = 'Main'),
    path('product/',views.Product,name = 'Product')
]

# 404 handler