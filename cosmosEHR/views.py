from django.shortcuts import render, redirect


def homepage(request):
    # If the user is already logged in, do not show them the landing page,
    # instead, send them to clinical tools home.
    if request.user.is_authenticated:
        return redirect('clinical/home')

    return render(request, 'homepage.html')







