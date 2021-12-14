from django.urls import path
from . import views
from .views import BlogListView,BlogDetailView
urlpatterns = [
    path('', views.main, name="main"),
    path('Aboutus/', views.aboutus, name="aboutus"),
    path('TOGBO/', views.togbo, name="togbo"),
    path('Contacts/', views.contacts, name='contacts'),
    path('MarksHBO/', views.marksgbo, name='markshbo'),
    path('MarksHBO/BRC', views.brc, name='brc'),
    path('MarksHBO/Digitronic', views.digitronic, name='digitronic'),
    path('MarksHBO/Atiker',views.atiker,name='atiker'),
    path('MarksHBO/Lovato',views.lovato,name='lovato'),
    path('blog/all',BlogListView.as_view(),name = 'blog'),
    path('blog/<int:pk>',BlogDetailView.as_view()),
    path('MarksHBO/OMVL',views.omvl,name='omvl'),
    path('Warranty/',views.warranty,name='warranty'),
    path('shop1/', views.shop1, name='shop1'),
    # path('accounts/', views.accounts, name='accounts')
]
