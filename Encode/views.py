from django.shortcuts import render
from .forms import ImageForm
# Create your views here.
def picture(request):
    if request.method == "POST":
        pass
    else:
        form = ImageForm()
        return render(request, 'Encode/picture.html', {'form': form})
