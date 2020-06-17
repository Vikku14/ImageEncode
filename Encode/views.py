from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from base64 import b64encode
from hashlib import md5
from os import path
from .forms import ImageForm
from .models import ImageData

# Create your views here.
def picture(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                pic = request.FILES['photo']
                form_data =  form.save(commit=False)
                pic_read = pic.read()                        #convert into bite string
                hash_result = md5(pic_read)                 # md5
                bf = form_data.base64_format= b64encode(pic_read).decode('ascii')
                hf = form_data.hash_format = hash_result.hexdigest()            # update form fields
                form.save()
                messages.success(request, 'Image uploaded Successfully.')
                context={
                    'base64': bf,
                    'hash':hf,
                    'form': ImageForm()
                }
                return render(request, 'Encode/picture.html',context)
            except Exception as e:
                messages.error(request, 'Unexpected error! try again.'+ str(e))
            return redirect('Encode:picture')
        else:
            messages.error(request, "Error: Check the fields again before submitting again.")
            return render(request, 'Encode/picture.html', {'form': form})
    else:
        return render(request, 'Encode/picture.html', {'form': ImageForm()})
