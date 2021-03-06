from django.urls import reverse_lazy
from django.views import generic
from .models import Post


class IndexView(generic.ListView):
	model = Post
	paginate_by = 5
	ordering = ['-updated_at'] # 並び順を更新時刻が新しい順にカスタマイズ
	template_name = 'blogs/index.html'


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/detail.html'


class CreateView(generic.edit.CreateView):
    model = Post
    fields = '__all__'  # ['title', 'text', 'author']
    template_name = 'blogs/create.html'


class UpdateView(generic.edit.UpdateView):
    model = Post
    fields = '__all__'  # ['title', 'text', 'author']
    template_name = 'blogs/update.html'


class DeleteView(generic.edit.DeleteView):
    model = Post
    success_url = reverse_lazy('blogs:index') # 削除完了時に遷移するページを指定
    template_name = 'blogs/delete.html'
