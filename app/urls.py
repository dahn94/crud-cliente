from django.urls import path
from django.contrib.auth.decorators import login_required


from .views import IndexView, CreateClienteView, UpdateClienteView, DeleteClienteView

urlpatterns = [
    path('', login_required(IndexView.as_view(template_name="index.html"))),
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateClienteView.as_view(), name='add_cliente'),
    path('<int:pk>/update/', UpdateClienteView.as_view(), name='upd_cliente'),
    path('<int:pk>/delete/', DeleteClienteView.as_view(), name='del_cliente'),
]
