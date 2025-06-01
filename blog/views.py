from django.shortcuts import render

posts = [
    {
        'author': 'Lucian',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '1st June, 2025'
    },
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '2nd June, 2025'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': '3rd June, 2025'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})