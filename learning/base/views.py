from django.shortcuts import render
from .models import Room

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
#     rooms = [
#     {'id':1, 'name':'Room 1'},
#     {'id':2, 'name':'Room 2'},
#     {'id':3, 'name':'Room 3'},
#     {'id':4, 'name':'Room 4'},
#     {'id':5, 'name':'Room 5'},
    
#    ]
   
    return render(request, 'base/room.html',{'rooms':rooms})
        

