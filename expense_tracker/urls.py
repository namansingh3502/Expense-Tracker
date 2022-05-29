from django.urls import path

from .views import *

urlpatterns = [
    path('newGroup', GroupTracker.as_view(), name="Add_Group"),
    path('<str:group_name>/add', ExpenseTracker.as_view(), name="Add_Expense"),
    path('<str:group_name>/update', ExpenseTracker.as_view(), name="Update_Expense"),
    path('<str:group_name>/<str:expense_name>/delete', ExpenseTracker.as_view(), name="Delete_Expense"),
    path('<str:group_name>/expense_detail', GroupTracker.as_view(), name="Group_Expense_Details")
]
