from django.template import RequestContext
from django.shortcuts import render
from django.http import Http404
# Create your views here.
from blog.forms import CommentForm
from .models import Blog, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User, Group
from blog.models import Blog, Category, Comment, Tag
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, CategorySerializer, BlogSerializer, CommentSerializer, TagSerializer


'''def get_blogs(request):
    blog_list = Blog.objects.all().order_by('-created')
    paginator = Paginator(blog_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    ctx = {
        'blogs': contacts
    }
    return render(request, 'blog_list.html', ctx)
    #return render_to_response('blog_list.html', {'object_list': ctx}, context_instance=RequestContext(request))


def get_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog_detail.html', ctx)
'''
class UserViewSet(viewsets.ModelViewSet):
    """
    API端：允许查看和编辑用户
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API端：允许查看和编辑组
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created')
    serializer_class = BlogSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer