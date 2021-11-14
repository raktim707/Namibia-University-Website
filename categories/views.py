from django.shortcuts import render, get_object_or_404, redirect

#import categories
from .models import Categories

# Create your views here.

def cat_list(request):

 # login check start
 if not request.user.is_authenticated :
  return redirect('mylogin')
 # login check end

 categories = Categories.objects.all()
 return render(request, 'back/category_list.html', {'categories':categories})

def cat_add(request):

 # login check start
 if not request.user.is_authenticated :
  return redirect('mylogin')
 # login check end

 if request.method == 'POST':

  name = request.POST.get('name')

  if name == "" :

   error = "All Fields Required"
   return render(request, 'back/error.html', {'error':error})

  if len(Categories.objects.filter(name=name)) != 0 :

   error = "This Name has been used before"
   return render(request, 'back/error.html', {'error':error})

  b = Categories(name=name)
  b.save()
  return redirect('cat_list')
 
 return render(request, 'back/category_add.html')

def cat_delete(request,pk):

 b = Categories.objects.filter(pk=pk)
 b.delete()

 return redirect('cat_list')