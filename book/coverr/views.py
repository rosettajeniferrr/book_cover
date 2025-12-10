from django.shortcuts import render

def book_preview(request):
    return render(request, 'bookcover.html')
