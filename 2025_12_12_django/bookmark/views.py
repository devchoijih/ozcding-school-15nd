from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from bookmark.models import Bookmark


# Create your views here.

def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    # SELECT * FROM bookmark;

    context = {
        "bookmarks":bookmarks
    }

    return render(request, "bookmark_list.html", context)

def bookmark_detail(request, pk):
    # try:
    #     bookmark = Bookmark.objects.get(pk=pk)
    # except:
    #     return Http404

    bookmark = get_object_or_404(Bookmark, pk=pk)

    context = {'bookmark' : bookmark}

    return render(request, "bookmark_detail.html", context)
