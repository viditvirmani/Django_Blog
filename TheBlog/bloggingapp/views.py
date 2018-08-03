# Create your views here.
from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import Post
from django.utils import timezone
from .forms import postform

def post_list(request):
    posts = Post.objects.all()
    return render(request,'bloggingapp/post_list.html',{'posts' : posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'bloggingapp/post_detail.html',{'post':post})

#TOOK HELP HERE A BIT
def post_new(request):
    if(request.method== "POST"):
        form = postform(request.POST)
        if(form.is_valid()):
            post=form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = postform()
    return render(request,'bloggingapp/add_info_in_post.html',{'form':form})

def post_delete(request,pk):
    Post.objects.filter(pk=pk).delete()
    return HttpResponse("deleted")
