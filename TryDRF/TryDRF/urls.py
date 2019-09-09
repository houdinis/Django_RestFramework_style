from django.conf.urls import url, include
from django.contrib import admin
from app01 import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'publisher', views.PublisherViewSet)
router.register(r'books', views.BooksViewSet)

urlpatterns = [
    # view_url
    # url(r'^publisher/$', views.Publisher_list.as_view(), name='publisher-list'),
    # url(r'^publisher/(?P<pk>[0-9]+)/$', views.Publisher_detail.as_view(), name='publisher-detail'),
    # url(r'^books/$', views.Books_list.as_view(), name='books-list'),
    # url(r'^books/(?P<pk>[0-9]+)/$', views.Books_detail.as_view(), name='books-detail'),

    # viewset_url
    url(r'^', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='图书管理系统')),
    url(r'^auth-api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),

]
