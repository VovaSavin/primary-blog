from django.urls import path
from .import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('blogs/', views.BlogsList.as_view(), name='blogs-all'),
    path('blogs/<int:pk>/', views.BlogsDetail.as_view(), name='blogs-detail'),
    path('blogers/', views.BlogerList.as_view(), name='blogers-all'),
    path('blogers/<int:pk>/', views.BlogerDetail.as_view(), name='blogers-detail'),
    path('create/', views.CreateBlog.as_view(), name='create-blog'),
    path('delete-blog/<int:pk>', views.DeleteBlog.as_view(), name='delete-blog'),
    path('my_profile/', views.my_pofile, name='profile'),
    path('my_profile/create-blogger/', views.edit_profile_info, name='profile-create'),
    path('blogs/<int:pk>/<slug:type>/', views.delete_comment, name='delete-comment'),
]
