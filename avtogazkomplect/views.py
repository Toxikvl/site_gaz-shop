from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView
from avtogazkomplect.models import Blog

class BlogListView(generic.ListView):
    model = Blog
    template_name = '../templates/html/blog_list.html'
    context_object_name = 'blog_list'
    queryset = Blog.objects.all()

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = '../templates/html/blog_detail.html'
def main(request,*args,**kwargs):
    return render(request,'../templates/html/Main.html',{})
def aboutus(request,*args,**kwargs):
    return render(request,'../templates/html/Aboutus.html',{})
def togbo(request,*args,**kwargs):
    return render(request,'../templates/html/TOGBO.html',{})
def contacts(request,*args,**kwargs):
    return render(request,'../templates/html/Contacts.html',{})
def marksgbo(request,*args,**kwargs):
    return render(request,'../templates/html/MarksGBO.html',{})
def brc(request,*args,**kwargs):
    return render(request,'../templates/html/BRC.html',{})
def digitronic(request,*args,**kwargs):
    return render(request,'../templates/html/Digitronic.html',{})
def atiker(request,*args,**kwargs):
    return render(request,'../templates/html/Atiker.html',{})
def lovato(request,*args,**kwargs):
    return render(request,'../templates/html/LOVATO.html')
def omvl(request,*args,**kwargs):
    return render(request,'../templates/html/OMVL.html')
def warranty(request,*args,**kwargs):
    return render(request,'../templates/html/Warranty.html')


def shop1(request):
    print('!!!!!!')
    return redirect('http://localhost:8000/shop')
