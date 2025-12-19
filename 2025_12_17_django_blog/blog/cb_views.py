from django.db.models import Q
from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogListView(ListView):
    #model = Blog
    queryset = Blog.objects.all()
    template_name = 'blog_list.html'
    paginate_by = 10
    ordering = ('-id', )

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q)  |
                Q(content__icontains=q)
            )

        return queryset

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    pk_url_kwarg = 'id'

    # def get_object(self, queryset=None):
    #     object = super().get_object()
    #     object = self.model.objects.get(pk=self.kwargs.get('id'))
    #
    #     return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'CBV'
        return context