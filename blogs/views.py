from django.shortcuts import render , redirect,get_object_or_404
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import *
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from .cart import Cart

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
          try :
               
               comments = Comments.objects.filter(which_post=pid, status=True)
               cat = Category.objects.all()
               replay = Replay.objects.all()
               post = Post.objects.get(id=pid, status=True)
               posts = Post.objects.filter(status=True)
               postss = Post.objects.all()
               unique_authors = set(post.author for post in postss)
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
                    'unique_authors': unique_authors,
               }
               return render(req, 'blog/blog-details.html', context=context)
          except:
               return render(req, 'blog/404.html')
     elif req.method == 'POST':
          form = CommentForm(req.POST)
          posts1 = Post.objects.get(id=pid)
          if form.is_valid():
               com = form.save(commit=False)
               com.which_post = posts1  # Set the which_comment field to the comment instance
               com.save()
               messages.add_message(req,messages.SUCCESS,'your comment submited')
               return redirect(req.path_info)
          else:
               messages.add_message(req,messages.ERROR,'your comment is invalid')
               return redirect(req.path_info)
     

def replay(req, cid):
     comment = Comments.objects.get(id=cid,status = True)
     if req.method == 'GET':
          context = {
               'comment' : comment,
          }
          return render(req, 'blog/reply.html', context=context)   
     
     elif req.method == 'POST':
          form = ReplayForm(req.POST)
          if form.is_valid():
              replay = form.save(commit=False)
              replay.which_comment = comment  # Set the which_comment field to the comment instance
              replay.save()
              pid = comment.which_post.id
              return redirect(f'/blogs/post_details/{pid}')
          else:
               messages.add_message(req,messages.ERROR,'your reply is invalid')
               return redirect(req.path_info)
 
def delete(req,cid):
    comment = Comments.objects.get(id=cid)
    print(f'cidedelete:{cid}')
    cidd = comment.which_post.id
    comment.delete()
    return redirect(f'/blogs/post_details/{cidd}') 
     

def edit(req, cid):
    comment = Comments.objects.get(id=cid)

    if req.method == 'GET':
        form = CommentForm(instance=comment)
        context = {
            'comment': comment,
            'form': form,
        }
        return render(req, 'blog/commentedit.html', context=context)
    
    elif req.method == 'POST':
        form = CommentForm(req.POST, instance=comment)
        if form.is_valid():
            form.save()
            eid = comment.which_post.id
            return redirect(f'/blogs/post_details/{eid}')  # Return an HttpResponse object after saving the form
        else:
            # Handle form validation errors if needed
            # You can render the form again with validation errors
            context = {
                'comment': comment,
                'form': form,
            }
            return render(req, 'blog/commentedit.html', context=context)
          

class PostListView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'post'
    paginate_by = 3

    def get_queryset(self):
        if self.kwargs.get('cat'):
            return Post.objects.filter(category__name=self.kwargs.get('cat'))
        elif self.kwargs.get('teacher'):
            return Post.objects.filter(auther__info = self.kwargs.get('auther'))
        elif self.request.GET.get('search'):
            return Post.objects.filter(content__contains = self.request.GET.get('search'))
        else:
            return Post.objects.filter(status=True) 
    def post(self, request, *args, **kwargs):
        post_detail = PostDetailView()
        return post_detail.post(request,*args,**kwargs)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog-details.html'
    context_object_name = 'blog'

    
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        if 'id' in request.POST :
            product = get_object_or_404(Post, id=request.POST['id'])    
            cart.delete_from_cart(product)       
        else:
            product = get_object_or_404(Post, id=request.POST['pk'])
            cart.add_to_cart_one_quatity(product)

        print(cart)
        return redirect(request.path_info)



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
               return redirect('/blogs/')
          


class PaymentView(TemplateView):
    template_name = 'blog/cart.html'
    def query_set(self):
        cart = Cart(self.request)
        return cart