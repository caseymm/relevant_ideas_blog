# Create your views here.
from blogApp.models import Posts
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post(request, pk):
    post = get_object_or_404(Posts, id=pk)

    context = {
        'post': post,
    }
    return render(request, "blogApp/post.html", context)
    

def all_posts(request):
    post_list = Posts.objects.all()
    paginator = Paginator(post_list, 25)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
         #If page is not an integer, deliver first page
        posts = paginator.page(1)
        
    except EmptyPage:
        #If page is out of range (e.g. 9999), deliver last page of results
        posts = paginator.page(paginator.num_pages)

    
    context = {
        'posts': posts,
    }
    
    return render(request, 'blogApp/all_posts.html', context)



