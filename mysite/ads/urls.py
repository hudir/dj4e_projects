from django.urls import path, reverse_lazy
from . import views

app_name='ads'
urlpatterns = [
    path('', views.AdListView.as_view(), name='all'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ads_detail'),
    path('ad/create',
        views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ads_create'),
    path('ad/<int:pk>/update',
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ads_update'),
    path('ad/<int:pk>/delete',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ads_delete'),
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
