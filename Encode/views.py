from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from base64 import b64encode
from hashlib import md5
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
                pic_name = 'base64_'+pic.name.split('.')[0]

                form_data =  form.save(commit=False)

                pic_read = pic.read()
                encoded_file = ContentFile(b64encode(pic_read))
                hash_result = md5(pic_read)

                form_data.base64_format= fs.save(pic_name, encoded_file)
                form_data.hash_format = hash_result.hexdigest()

                form.save()
                messages.success(request, 'Image uploaded Successfully.')

            except Exception as e:
                messages.error(request, 'Unexpected error! try again.'+ str(e))

            return redirect('Encode:picture')
        else:
            messages.error(request, "Error: Check the fields again before submitting again.")
            return render(request, 'Encode/picture.html', {'form': form})
    else:

        return render(request, 'Encode/picture.html', {'form': ImageForm()})
