from django import contrib
from django.http import HttpResponse
from django.http.response import Http404
from amapp import models
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.utils.decorators import method_decorator
from datetime import datetime
import amapp
from .decorators import register_signin_required
from .models import Register, Session

# Create your views here.
def index(request):
    return render(request, template_name='amapp/index.html')


class LoginView(View):
    def get(self,request):
        return render(request, template_name='amapp/login.html');

    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # print(user)
            # print(request.session['_auth_user_id'])
            return redirect('amapp:admin_dashboard')
        else:
            try:
                register = get_object_or_404(Register,name=username, password=password)
                request.session['register_id'] = register.id
                return redirect('amapp:register_dashboard', pk=register.id)
            except Http404:
                messages.error(request, 'Invalid credentials')
                return render(request, template_name='amapp/login.html')


def logout_view(request):
    logout(request)
    return redirect('amapp:home')


@login_required
def admin_dashboard(request):
    return render(request, template_name='amapp/admin_dashboard.html')


@method_decorator(register_signin_required, name='dispatch')
class RegisterDashboard(generic.DetailView):
    model= Register
    template_name='amapp/dashboard.html'
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        session_count = Session.objects.filter(register_id=id).count()
        context['session_count']=session_count
        return context


@method_decorator(register_signin_required, name='dispatch')
class SessionListView(generic.ListView):
    model = Session
    template_name = 'amapp/mysessions.html'
    context_object_name = 'Context'

    def get_queryset(self):
        register = Register.objects.get(id = self.kwargs['pk'])
        sessions = Session.objects.filter(register_id=self.kwargs['pk']).order_by('id').reverse()
        context = {'Register':register, 'Sessions':sessions}
        print(context)
        return context


@method_decorator(register_signin_required, name='dispatch')
class SessionDetailsView(generic.DetailView):
    model = Session
    template_name = 'amapp/session_details.html'
    context_object_name = 'session'
    
    # def get_queryset(self):
    #     session = Session.objects.get(id = self.kwargs['sid'])
    #     attendees = 


def addstudent(request):
    return render(request, template_name='amapp/addstudent1.html')


class CreateRegisterView(View):
    def get(self,request):
        return render(request, template_name='amapp/create_register.html');

    def post(self,request):
        reg_name=request.POST['reg_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1 == password2:
            new_register = Register(name=reg_name, password=make_password(password1))
            new_register.save()
            messages.success(request, 'Register created successfully!')
            request.session['register_id'] = new_register.id
            return redirect('amapp:register_dashboard', pk=new_register.id)
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, template_name='amapp/create_register.html');



def  start_session(request):
    if request.method == 'POST':
        reg_name = request.POST['register-name']
        device_id = request.POST['device-id']
        title = request.POST['title']
        start_time = request.POST['start-time']
        end_time = request.POST['end-time']
        password = request.POST['password']
        date = datetime.now().date()
        
        register = Register.objects.get(name = reg_name)
        new_session = Session(title = title,date = date,start = start_time,\
            end = end_time,register = register)
        new_session.save()
        return HttpResponse('got the form')