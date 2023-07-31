from django.shortcuts import render
from .models import About


def about_wells(request, *args, **kwargs):
    about = About.objects.all().first()

    return render(
        request,
        "about.html",
        {
            "about": about
        },
    )
