from django.shortcuts import render

# Create your views here.
def picture(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'Encode/picture.html')
