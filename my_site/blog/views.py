from django.shortcuts import render,get_object_or_404

from . models import Post

# Create your views here.



def starting_page(request):
    latest_post=Post.objects.all().order_by('-date')[:3]
    return render(request,"blog/index.html",{
        'last_post':latest_post
    })

def posts(request):
    data=Post.objects.all().order_by('-date')
    return render(request,"blog/all-posts.html",{
    'all_post':data
    })

def post_details(request,slug):
    identify_post=get_object_or_404( Post,slug=slug)
    return render(request,"blog/post-detail.html", {
        'post':identify_post,
        'post_tag':identify_post.tags.all()
    })
