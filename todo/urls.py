from django.urls import path
from todo import views

urlpatterns = [
    path("",views.ListTodoAPIView.as_view(),name="todo_list"),
    path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
    path("view/<int:pk>/", views.RetrieveTodoAPIView.as_view(), name="todo_view"),
    path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_todo"),
    path("category/",views.ListCategoryAPIView.as_view(),name="category_list"),
    path("category/<int:pk>/",views.RetrieveCategoryAPIView.as_view(),name="category_single"),
    path("category/<int:pk>/products/",views.CategoryProductsView.as_view(),name="category_product_list"),
    path("users/",views.ListUserAPIView.as_view(),name="users_list"),
    path("users/<int:pk>/",views.UserDetailAPIView.as_view(),name="users_detail"),    
    path("users/products/<int:pk>/",views.UserProductsAPIView.as_view(),name="users_products"),
    path("users/products/",views.CurrentUserProductsAPIView.as_view(),name="users_product"),

]