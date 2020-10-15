from django.shortcuts import render,redirect
from .models import *
from .form import *
import math
# Create your views here.
def index(request):
    categoryList = Category.objects.all()
    context = {'categoryList':categoryList}
    return render(request,'category/list.html',context)

def createCategory(request):
    form =  CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}        
    return render(request,'category/category_form.html',context)

def updateCategory(request,pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance=category)
    if request.method== 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'category/category_form.html',context)

def deleteCategory(request,pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('/')

def listProduct(request):
    productList = Product.objects.all()
    context = {'productList':productList}
    return render(request,'product/product_list.html',context)

def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    context = {'form':form}
    return render(request,'product/product_form.html',context)

def updateProduct(request,pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if  form.is_valid():
            form.save()
            return redirect('list-product')
    context = {'form':form}
    return render(request,'product/product_form.html',context)

def deleteProduct(request,pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('list-product')