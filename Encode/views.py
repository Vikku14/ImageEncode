from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from base64 import b64encode
from hashlib import md5
from os import path
from rest_framework import status
from .forms import ImageForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import ImageSerializer, ImagePostSerializer
from .models import ImageData
from rest_framework.parsers import FileUploadParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
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
                form_data.base64_format= b64encode(pic_read).decode('ascii')
                form_data.hash_format = hash_result.hexdigest()            # update form fields
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



class ImageApi(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request):
        images = ImageData.objects.all()
        ser = ImageSerializer(images, many= True)
        return Response(ser.data)

    @csrf_exempt
    def post(self, request):
        serializer = ImageSerializer(data = request.data)

        if serializer.is_valid():
            try:
                pic = request.data['photo']
                pic_read = pic.read()
                pic_readed = b64encode(pic_read)
                hash_result = md5(pic_read)                 # md5
                serializer.save(photo = pic)
                                #convert into bite string
                serializer.save(base64_format = pic_readed.decode('ascii'), hash_format=hash_result.hexdigest() )

                return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
