from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory
from .models import Meeting, Room
def detail(request,id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request,"meetings/detail.html",{"meeting":meeting})

def rooms_list(request):
    return render(request, "meetings/room_list.html",
                  {"rooms": Room.objects.all()})

def room_detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/room_detail.html", {"room": room})

def new(request):
    return render(request, "meetings/new.html")

# Create your views here.
