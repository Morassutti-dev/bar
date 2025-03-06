from . import views
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('', lambda request: redirect('/login/')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('comanda/criar/', views.criar_comanda, name='criar_comanda'),
    path('comanda/<int:comanda_id>/', views.detalhes_comanda, name='detalhes_comanda'),
    path('comanda/<int:comanda_id>/adicionar/', views.adicionar_item, name='adicionar_item'),
    path('comandas/', views.listar_comandas, name='listar_comandas'),
    path('comandas/detalhes/<int:comanda_id>/', views.detalhes_comanda, name='detalhes_comanda'),
    path('comandas/editar/<int:comanda_id>/', views.editar_comanda, name='editar_comanda'),
    path('comandas/excluir/<int:comanda_id>/', views.excluir_comanda, name='excluir_comanda'),
    path('item/excluir/<int:item_id>/', views.excluir_item, name='excluir_item'),
    path('comandas/editar-cliente/<int:comanda_id>/', views.editar_cliente, name='editar_cliente'),
    
]
