from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.views import generic
from .forms import CustomerSignupForm
from .models import Customer,FitnessPlan
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

def home(request):
    plans = FitnessPlan.objects 
    return render(request,'plans/home.html',{'plans':plans})
    
def plan(request,pk):
    plan = get_object_or_404(FitnessPlan,pk=pk)
    ## if the plan he choose if premium
    if plan.premium:
        ## check if the user is authenticated
        ## without authentication and membership cant see the 
        ## premium plan
        if request.user.is_authenticated:
            try:
                if request.user.customer.membership:
                    return render(request,'plans/plan.html',{'plan':plan})
            except Customer.DoesNotExist:
                return redirect('join')
        return redirect('join')
    else:
        return render(request,'plans/plan.html',{'plan':plan})
        
        
## you can do it in the function 
class SignUp(generic.CreateView):
    form_class = CustomerSignupForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'
    
    ## this is a default function
    ## in class based view
    def form_valid(self, form):
        ## passing to the base class
        ## valid variable will be boolean
        valid = super(SignUp,self).form_valid(form)
        username,password = form.cleaned_data.get('username'),form.cleaned_data.get('password')
        
        ## create the new user
        new_user = authenticate(username=username,password = password)
        ## login the user
        
        ## self.request have to be passed
        login(self.request,new_user)
        return valid 
        
def join(request):
    return render(request,'plans/join.html')
        
        
def checkout(request):
    return HttpResponse("you are in the checkout page")

def settings(request):
    return HttpResponse("you are in the Settings page")

