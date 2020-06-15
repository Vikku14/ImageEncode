from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import base64
from os import path
from django.core.files.base import ContentFile
from .forms import ImageForm
# Create your views here.
def picture(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                fs = FileSystemStorage(location=path.join(settings.MEDIA_ROOT, 'Base64'))
                pic = request.FILES['photo']
                pic_name = 'base64'+pic.name.split('.')[0]

                form_data =  form.save(commit=False)

                encoded_string = ContentFile(base64.b64encode(pic.read()))

                form_data.base64_format= fs.save(pic_name, encoded_string)

                form.save()
            except:
                messages.error(request, 'Unexpected error! try again.')
                
            return redirect('Encode:picture')
        else:
            messages.error(request, "Error: Check the fields again before submitting again.")
            return render(request, 'Encode/picture.html', {'form': form})
    else:
        form = ImageForm()
        return render(request, 'Encode/picture.html', {'form': form})
