# myapp/views.py
from django.shortcuts import redirect, render
from django.contrib.auth import logout

from .models import Memory
from .forms import MemoryModelForm

def home_view(request):
    """
    Home view
    """
    context = {'memories':[]}
    if request.user.is_authenticated:
        context['user'] = request.user
        try:
            memories = Memory.objects.filter(user = request.user)
            for memory in memories:
                context['memories'].append(memory)
            if len(context['memories']) != 0:
                return render(request, "myapp/home.html", {'context': context})
            else:
                context['mess'] = "YOU HAVE NO MEMORIES"
                return render(request, "myapp/home.html", {'context': context})
        except:
            context['mess'] = "YOU HAVE NO MEMORIES"
            return render(request, "myapp/home.html", {'context': context})
    else:
        context['mess'] = "YOU HAVE TO LOGIN"
        return render(request, "myapp/home.html", {'context': context})
    
def create_view(request):
    """
    Create View
    """
    if request.user.is_authenticated:
        context ={}
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

