from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id':1, 'name':'Room 1'},
#     {'id':2, 'name':'Room 2'},
#     {'id':3, 'name':'Room 3'},
#     {'id':4, 'name':'Room 4'},
#     {'id':5, 'name':'Room 5'},
    
# ]
# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def room_page(request,pk):
    
    
   
    room = Room.objects.get(id=pk)
    
  
    return render(request, 'base/room.html',{'room':room})



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