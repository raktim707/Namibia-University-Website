from django.shortcuts import render, get_object_or_404, redirect

#import categories
from .models import SubCategories
from categories.models import Categories 

# Create your views here.

def subcat_list(request):
 # login check start
 if not request.user.is_authenticated :
  return redirect('mylogin')
 # login check end

 subcategories = SubCategories.objects.all()
 return render(request, 'back/subcategory_list.html', {'subcategories':subcategories})

def subcat_add(request):
 # login check start
 if not request.user.is_authenticated :
  return redirect('mylogin')
 # login check end

 categories = Categories.objects.all()

 if request.method == 'POST':

  
  name = request.POST.get('name')
  catid = request.POST.get('categories')

  if name == "" :

   error = "All Fields Required"
   return render(request, 'back/error.html', {'error':error})

  if len(SubCategories.objects.filter(name=name)) != 0 :

   error = "This Name has been used before"
   return render(request, 'back/error.html', {'error':error})

  catname = Categories.objects.get(pk=catid).name

  b = SubCategories(name=name, catname=catname, catid=catid)
  b.save()
  return redirect('subcat_list')
  
 
 return render(request, 'back/subcategory_add.html', {'categories':categories})

def subcat_del(request,pk) :

 b = SubCategories.objects.filter(pk=pk)
 b.delete()

 return redirect('subcat_list')