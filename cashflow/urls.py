from django.urls import path
from . import views

urlpatterns = [
    # CashFlowSection URLs
    path('', views.index, name='index'),
    path('sections/', views.section_list, name='section_list'),
    path('sections/create/', views.section_create, name='section_create'),
    path('sections/<int:pk>/edit/', views.section_update, name='section_update'),
    path('sections/<int:pk>/delete/', views.section_delete, name='section_delete'),

    # Transaction URLs
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/create/', views.transaction_create, name='transaction_create'),
    path('transactions/<int:pk>/edit/', views.transaction_update, name='transaction_update'),
    path('transactions/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),

    # CashFlowStatement URLs
    path('statements/', views.statement_list, name='statement_list'),
    path('statements/create/', views.statement_create, name='statement_create'),
    path('statements/<int:pk>/', views.statement_detail, name='statement_detail'),
    path('statements/delete/<int:pk>/', views.statement_delete, name='statement_delete'),
 

]
