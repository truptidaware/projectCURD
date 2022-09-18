from django.shortcuts import render
from .models import prod
from .forms import ProdForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(r):
    obj = prod.objects.all()
    return render(r,'curdapp/index.html',{'obj':obj})

def insert(r):
    form = ProdForm()
    if r.method =='POST':
        form = ProdForm(r.POST)
        if form.is_valid():
            form.save(commit=True)
        return HttpResponseRedirect('/')
    return render(r,'curdapp/insert.html',{'form':form})

def delete(r,id):
    prd = prod.objects.get(id=id)
    prd.delete()
    return HttpResponseRedirect('/')

def update(r,id):
        prd = prod.objects.get(id=id)
        form= ProdForm()
        if r.method == 'POST':
            form = ProdForm(r.POST, instance=prd)
            if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect('/')
        return render(r,'curdapp/update.html', {'prd':prd})
