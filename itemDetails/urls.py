from django.conf.urls import url
from . import views
from django.urls import path

app_name='itemDetails'
urlpatterns = [
    path('', views.index, name='itemDetails'),
   # /itemDetails/2
   # path('<article_id>/', views.getArticleDetails, name='articleid'),

    # /itemDetails/additem
    path('addItem/', views.addItem, name='addItem'),


    # /itemDetails/additem/deleteitem
    path('addItem/<pk>/delete/', views.ItemListDelete.as_view(), name='deleteItem'),

    #/itemDetails/search
    path('search/', views.search, name='searchItem')

]