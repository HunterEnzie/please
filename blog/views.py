from django.shortcuts import render

# Create your views here.

posts = [
	{ 
		'title': 'My First Beautiful Soup Project',
		'content': "I don't know what it will be yet",
		'date_posted': '1/6/2020'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def contact(request):
	return render(request, 'blog/contact.html', {'title': 'Contact'})

def stories(request):
	return render(request, 'blog/stories.html', {'title': 'Stories'})