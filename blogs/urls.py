from django.urls import path
from . import views


app_name = 'blogs'
 
urlpatterns = [
	# 一覧表示のURL: /
	path('', views.IndexView.as_view(), name='index'),

	# 新規作成のURL: /post/create/
	path('post/create/', views.CreateView.as_view(), name='create'),

	# 詳細表示のURL: /post/123/
	path('post/<int:pk>/', views.DetailView.as_view(), name='detail'),

	# 内容更新のURL: /post/123/update/
	path('post/<int:pk>/update/', views.UpdateView.as_view(), name='update'),

	# 記事削除のURL: /post/123/delete/
	path('post/<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]
