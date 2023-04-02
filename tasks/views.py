from django.shortcuts import redirect, render,HttpResponse
from .models import Task
# Create your views here.
def index(request):
    if request.method=='POST':
        if request.POST.get('name'):
            task=Task()
            task.name=request.POST.get('name')
            task.save()
            return redirect('/')
    data=Task.objects.all()
    context={
        'list':data,
    }
    return render(request,'index.html',context)

def delete(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('/')