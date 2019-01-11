from django.shortcuts import render, HttpResponse

def index(request):
    import pdb;pdb.set_trace()
    return render(request,'loginpage/home.html')
