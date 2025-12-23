from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import CommentForm
from blog.models import Blog, Comment


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
        context['comment_form'] = CommentForm()
        context['comments'] = Comment.objects.filter(blog_id=self.kwargs['id'])
        return context

    def post(self, *args, **kwargs):
        comment_form = CommentForm(self.request.POST)

        if not comment_form.is_valid():
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            context['comment_form'] = comment_form
            return self.render_to_response(context)

        if not self.request.user.is_authenticated:
            raise Http404

        comment = comment_form.save(commit=False)
        comment.blog_id = self.kwargs['id']
        comment.author = self.request.user
        comment.save()

        return HttpResponseRedirect(reverse_lazy('blog:detail', kwargs={'id': self.kwargs['id']}))

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ('title', 'content')
    #success_url = reverse_lazy('blog:list', k)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'id': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_title'] = "작성"
        context['btn_name'] = "생성"
        return context

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ('title', 'content')
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if self.object.author != self.request.user:
            raise Http404

        return self.object

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'id': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_title'] = "수정"
        context['btn_name'] = "수정"
        return context


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if self.object.author != self.request.user:
            raise Http404

        return self.object

    def get_success_url(self):
        return reverse_lazy('blog:list')