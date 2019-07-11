from django.urls import path
from . import views 
from . views import HomeView,BlogCreateView,AllBlogView,BlogDetailView,BlogUpdateView,BlogDeleteView
from django.contrib.auth import views as auth_view

app_name = 'blog'

urlpatterns = [
	path('', HomeView.as_view(), name = 'home'),
	path('blog-create/', BlogCreateView.as_view(), name = 'create_blog'),
	path('login/', auth_view.LoginView.as_view(template_name = 'blog/login.html'), name = 'login'),
	path('logout/', auth_view.LogoutView.as_view(template_name = 'blog/logout.html'), name = 'logout'),
	path('all-blogs/',AllBlogView.as_view(), name = 'all-blogs'),
	path('<int:pk>/detail/', BlogDetailView.as_view(), name = 'detail'),
	path('<int:pk>/update/',BlogUpdateView.as_view(),name = 'blog-update'),
	path('<int:pk>/delete/', BlogDeleteView.as_view(),name = 'blog-delete'),
	path('signup/', views.sign_up, name = 'signup'),

]