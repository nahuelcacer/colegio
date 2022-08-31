from django.shortcuts import render, redirect
from django.views import View
from apps.personal.models import Personal
from apps.personal.forms import AgregarPersonal
# Create your views here.
class AddPersonal(View):
    def get(self,request,*args, **kwargs):
        personal = Personal.objects.all()
        form = AgregarPersonal()
        context = {
            'form':form,
            'personal':personal
        }
        return render(request, 'personal/listarPersonal.html', context)

    def post(self,request,*args, **kwargs):
        form = AgregarPersonal(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apps.personal:listarPersonal',) 