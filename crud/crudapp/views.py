from django.shortcuts import render,redirect
from crudapp.models import employee
from crudapp.forms import employeeform
from django.db.models import Q,Count
# Create your views here.
def empview(request):
    emp=employee.objects.all()
    count=employee.objects.all().count()
    print(count)
    return render(request,'test/home.html',{'employee':emp,'count':count})

def empadd(request):
    form=employeeform()
    if request.method=='POST':
        form=employeeform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'test/add.html',{'form':form})

def delete(request,id):
    Employee=employee.objects.get(id=id)
    Employee.delete()
    return redirect('/')

def update(request,id):
    msg='update'
    emp=employee.objects.get(id=id)
    if request.method=='POST':
        print('posted')
        form=employeeform(request.POST,instance=emp)
        if form.is_valid():
            print('valid')
            form.save()
            print('saveed')
            return redirect('/')
    return render(request,'test/update.html',{'employee':emp,'msg':msg})




def empselectview(request):
    emp=employee.objects.filter(Q(esal__gt=1)&~Q(eaddr__exact='mumbai'))
    return render(request,'test/home.html',{'employee':emp})
