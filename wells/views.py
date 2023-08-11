from django.shortcuts import render


def err403(request, exception):

    return render(request, "errcodes/err403.html", status=403)


def err404(request, exception):

    return render(request, "errcodes/err404.html", status=404)


def err405(request, exception):

    return render(request, "errcodes/err405.html", status=405)


def err500(request):

    return render(request, "errcodes/err500.html", status=500)
