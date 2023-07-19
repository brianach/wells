from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from map.models import Well
from .models import Post
# from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "location": post.location,
                "comments": comments,
                "liked": liked,
            },
        )

# class WellDetail(View):
#    def get(self, request, *args, **kwargs):
# Retrieve all data from the Well model
#        well_data = Well.objects.values('well', 'townland', 'county', 'cures')
#        well_data_list = list(well_data)
# Pass the well_data to the specified template
#        return render(request, 'well.html', context={'well_data': well_data_list})
# for record in well_data:
#    addr_one = record['townland']
# return render(request, 'well.html', context={'addr_one': addr_one})
