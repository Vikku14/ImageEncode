from django.shortcuts import render
from django.contrib import messages

from .forms import ImageForm
# Create your views here.
def picture(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'Encode/picture.html', { 'form': ImageForm() })
        else:
            messages.error(request, "error")
            return render(request, 'Encode/picture.html', {'form': form})
    else:
        form = ImageForm()
        return render(request, 'Encode/picture.html', {'form': form})
