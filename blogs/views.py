from django.shortcuts import render , redirect
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import *
from django.contrib import messages


def blog_home(req, tag=None, username=None, cat=None):
    # Retrieve all posts with status=True
    posts = Post.objects.filter(status=True)

    # Retrieve all categories
    categories = Category.objects.all()

    # Retrieve all tags
    tags = Tags.objects.all()

    # Retrieve the last four posts
    last_four_posts = posts[:3]

    # Filter posts based on the provided tag, username, or category
    if tag:
        print(f"Filtering by tag: {tag}")
        posts = Post.objects.filter(tag__name=tag)
        print(f"Number of matching posts: {posts.count()}")



    if username:
        posts = Post.objects.filter(author__username=username)

    if cat:
     #     print(f"Filtering by category: {cat}")
         posts = Post.objects.filter(category__name=cat)
     #     print(f"Number of matching posts: {posts.count()}")

    # Filter posts based on search query if provided
    if req.GET.get('search'):
        posts = Post.objects.filter(title__contains=req.GET.get('search'))


    # Paginate the posts with 4 posts per page
    posts = Paginator(posts, 3)
    first_page = 1
    last_page = posts.num_pages
    try:
        page_number = req.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {
        'posts': posts,
        'first_page':first_page,
        'last_page':last_page,
        'category': categories,
        'last_four_posts': last_four_posts,
        'tags': tags,
        'cat': categories,  # Include the 'cat' variable in the context
    }

    return render(req, 'blog/blog.html', context=context)


def blog_single(req, pid):
     if req.method == 'GET':
          # try :

               comments = Comments.objects.filter(which_post=pid, status=True)
               cat = Category.objects.all()
               replay = Replay.objects.all()
               post = Post.objects.get(id=pid, status=True)
               posts = Post.objects.filter(status=True)
               postss = Post.objects.all()
               tags = Tags.objects.all()
               post_list_id = []
               p1 = Post.objects.filter(id=pid)
               for post in posts:
                    post_list_id.append(post.id)

               post_list_id.reverse()

               if post_list_id[0] == pid:
                    previous_post = None
                    next_post = posts.get(id=post_list_id[1])
                    
               elif post_list_id[-1] == pid:
                    previous_post = posts.get(id=post_list_id[-2])
                    next_post = None

               else:
                    next_post = posts.get(id=post_list_id[post_list_id.index(pid)+1])
                    previous_post =  posts.get(id=post_list_id[post_list_id.index(pid)-1])



               
               
               post.counted_views += 1
               post.save()
               context = {
                    'post': post,
                    'postss':p1,
                    'post1':postss,
                    'next' : next_post,
                    'prev' : previous_post,
                    'comments': comments,
                    'replay' : replay,
                    'tags': tags,
                    'cat': cat,
               }
               return render(req, 'blog/blog-details.html', context=context)
          # except:
          #      return render(req, 'blog/404.html')
     elif req.method == 'POST':
          form = CommentForm(req.POST)
          print(f"pid: {pid}")
          if form.is_valid():
               form.save()
               messages.add_message(req,messages.SUCCESS,'your comment submited')
               return redirect(req.path_info)
          else:
               messages.add_message(req,messages.ERROR,'your comment is invalid')
               return redirect(req.path_info)
     

def replay(req, cid):
     comment = Comments.objects.get(id=cid)
     if req.method == 'GET':
          form = ReplayForm()
          context = {
               'comment1' : comment,
               'form':form,
          }
          return render(req, 'blog/reply.html', context=context)   
     
     elif req.method == 'POST':
          form = ReplayForm(req.POST)
          if form.is_valid():
               form.save()
               ccid = comment.which_post.id
               return redirect(f'/blogs/post_details/{ccid}')
          else:
               messages.add_message(req,messages.ERROR,'your reply is invalid')
               return redirect(req.path_info)
 
def delete(req, cid):

     comment = Comments.objects.get(id=cid)
     comment.delete()
     return redirect('/')   
     

def edit(req, cid):
     comment = Comments.objects.get(id=cid)
     if req.method == 'GET':
          
          form = CommentForm(instance=comment)
          context = {
               'form' : form,
          }
          return render(req,'blog/commentedit.html',context=context)
     elif req.method == "POST" :
          form = CommentForm(req.POST, instance=comment)
          if form.is_valid():
               form.save()
               return redirect('/blog/')
          

def add(req):
     if req.method == 'GET':
          context = {
               'form' : PostForm()
          }
          return render(req,'blog/add.html',context=context)
     elif req.method == 'POST':
          form = PostForm(req.POST, req.FILES)
          
          if form.is_valid():
               form.save()
               return redirect('/blog/')
