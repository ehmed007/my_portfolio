from django.shortcuts import render
from django.http import HttpResponse
import PyPDF2

def index(request):
    return render(request, 'app/index.html')

def download_cv(request):
    cv = open('app/static/app/file/cv.pdf', 'rb')
    response = HttpResponse(cv.read(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ahmed_cv"'
    return response
