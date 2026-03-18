from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(
        published_at__lte=timezone.now()
    ).order_by('-published_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(
        Post,
        pk=pk,
        published_at__lte=timezone.now()
    )
    return render(request, 'blog/post_detail.html', {'post': post})


def post_list_api(request):
    posts = Post.objects.filter(
        published_at__lte=timezone.now()
    ).values('id', 'title', 'content', 'author__username', 'published_at')
    data = list(posts)
    return JsonResponse(data, safe=False)
