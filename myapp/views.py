# myapp/views.py
from django.shortcuts import redirect, render
from django.contrib.auth import logout

from .models import Memory
from .forms import MemoryModelForm

def home_view(request):
    context = {'memories':[]}
    if request.user.is_authenticated:
        context['user'] = request.user
    # Do something for authenticated users.
        # try:
        memories = Memory.objects.filter(user = request.user).first()
        context['memories'].append(memories)
        return render(request, "myapp/home.html", {'context': context})
        # except:
        #     context['mess'] = "YOU HAVE NO MEMORIES"
        #     return render(request, "myapp/home.html", {'context': context})
    else:
        # Do something for anonymous users.
        context['mess'] = "YOU HAVE TO LOGIN"
        return render(request, "myapp/home.html", {'context': context})
    
def create_view(request):
    if request.user.is_authenticated:
        context ={}
    
        # add the dictionary during initialization
        form = MemoryModelForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('app:home')

        context['form']= form
        return render(request, "myapp/create.html", context)
    else:
        context ={}
        context['mess'] = "YOU HAVE TO LOGIN"
        return render(request, "myapp/home.html", {'context': context})

def delete_view(request, pk):
    query = Memory.objects.filter(pk=pk)
    query.delete()
    return redirect('app:home')

def logout_view(request):
    logout(request)
    return redirect('app:home')

