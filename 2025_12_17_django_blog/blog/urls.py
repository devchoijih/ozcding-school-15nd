from django.urls import path
from blog import cb_views

urlpatterns = [
    path('', cb_views.BlogListView.as_view(), name='list'),
    path('<int:id>/', cb_views.BlogDetailView.as_view(), name='detail'),
    path('create/', cb_views.BlogCreateView.as_view(), name='create'),
    path('<int:id>/update', cb_views.BlogUpdateView.as_view(), name='update'),
    path('<int:id>/delete', cb_views.BlogDeleteView.as_view(), name='delete'),
]