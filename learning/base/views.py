from django.shortcuts import render,redirect
from .models import Room,Topic,User
from .forms import RoomForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# rooms = [
#     {'id':1, 'name':'Room 1'},
#     {'id':2, 'name':'Room 2'},
#     {'id':3, 'name':'Room 3'},
#     {'id':4, 'name':'Room 4'},
#     {'id':5, 'name':'Room 5'},
    
# ]
# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'base/home.html')

def room_page(request,pk):
    
    
   
    room = Room.objects.get(id=pk)
    topics = Topic.objects.all()
  
    return render(request, 'base/room.html',{'room':room,'topics':topics})



def room(request):
    
    
    rooms = Room.objects.all()

    return render(request, 'base/room.html',{'rooms':rooms})
        

def create_room(request):
    
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST) # the data will come up here!
        if form.is_valid(): # check validity of form!
            form.save() # if the form is ok then save in db!
            # after saving again send the empty form!
            # form = RoomForm()
            return redirect('room')
    # else:
        # form = RoomForm()
            
    context = {'form':form}
    return render(request, 'base/room_form.html',context)


def update_room(request,pk):
    # finding the specific room using pk!
    room = Room.objects.get(pk=pk)
    
    # creating a form and initializing that data!
    form = RoomForm(instance=room)
    
    # also now for handling request post!
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room) # the data will come up here!
        if form.is_valid(): # check validity of form!
            form.save() # if the form is ok then save in db!
            # after saving again send the empty form!
            # form = RoomForm()
            return redirect('room')
    
    context = {'form':room}

    return render(request, 'base/room_form.html',context)     

def delete_room(request,pk):
    room = Room.objects.get(pk=pk)
    if request.method == 'POST':
     room.delete() # delete this room!
     return redirect('room')  #return back to all rooms home-page!
     
    return render(request, 'base/delete.html',{'obj':room})