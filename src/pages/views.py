from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	# print(args, kwargs)
	# print(request.user)
	# return HttpResponse("<h1>Hello World!</h1>") #string of HTML code
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
	my_context = {
		"title": "i\'m using django.",
		"my_desc": "This is a template",
		"my_number": 312,
		"my_array": [121,343,566,789,12,"dfg"],
		"my_html": "<h2>Hey html</h2>"
	}

	return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
	return HttpResponse("<h1>Social page</h1>")
