from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView,CreateView,UpdateView,DetailView,View
from ebizApp.models import Categories, SubCategories,Products,ProductMedia
from django.db.models import Q
# Create your views here.
def demoPage(request):
    return render(request,"demo.html")

def adminSignin(request):
    return render(request,"admin_templates/signin.html")

def adminLoginProcess(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user= authenticate(request=request,username=username,password=password)
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("admin_home"))
    else:
        messages.error(request,"Error in login! Invalid login details")
        return HttpResponseRedirect(reverse('admin_login'))
    
def adminLogoutProcess(request):
    logout(request)
    messages.success(request,"Logout Successful")
    return HttpResponseRedirect(reverse("admin_login"))

class ProductListView(ListView):
    model=Products
    template_name="customer_templates/store.html"
    paginate_by=3
    def get_queryset(self):
        filter_val=self.request.GET.get("filter","")
        order_by=self.request.GET.get("orderby","id")
        if filter_val!="":
            products=Products.objects.filter(Q(product_name__contains=filter_val) | Q(product_description__contains=filter_val)).order_by(order_by)
        else:
            products=Products.objects.all().order_by(order_by)
        
        product_list=[]
        for product in products:
            product_media=ProductMedia.objects.filter(product_id=product.id,media_type=1,is_active=1).first()
            product_list.append({"product":product,"media":product_media})

        return product_list

    def get_context_data(self,**kwargs):
        context=super(ProductListView,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get("filter","")
        context["orderby"]=self.request.GET.get("orderby","id")
        context["all_table_fields"]=Products._meta.get_fields()
        return context
