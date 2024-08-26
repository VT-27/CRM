from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# vivek123/Bigboss@2627
# Create your views here.
def home(request):
    records = Record.objects.all()
    #check if person logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate user
        user=authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, "Successful Login")
            return render(request,'home.html')
        else:
            messages.success(request,"There was an error in logging, Try again")
            return render(request,'home.html')
    else:
        return render(request, 'home.html', {'records': records})
    

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out..")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        #Lookup the records
        customer_record = Record.objects.get(id = pk) # This fetches a single record. 
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You need to Login")
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_rec = Record.objects.get(id = pk)
        delete_rec.delete()
        messages.success(request, "Record Deleted Successfully.")
        return redirect('home')
    else:
        messages.success(request, "You need to Login")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Record Added Successfully")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in")
        return redirect('home')
    
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id = pk)
        form = AddRecordForm(request.POST or None, instance=current_record) # This line shows current record with the values held in it. On clicking hyperlink (1), forms open up and current record details are shown
        if form.is_valid():
            form.save()
            messages.success(request,"Record Updated Successfully")
            return redirect('home')
        return render(request,'update_record.html', {'form':form})
    else:
        messages.success(request,"You must be logged in")
        return redirect('home')
         
         