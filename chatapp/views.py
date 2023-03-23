from django.shortcuts import render
from django.http import HttpResponseForbidden

# Create your views here.

def course_chat_room(request, course_id):
	print("On the view")
	return render(request, 'chat/room.html', {'course': course_id})
