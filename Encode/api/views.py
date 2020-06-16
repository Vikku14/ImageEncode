from rest_framework.parsers import FileUploadParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import ImageSerializer
from base64 import b64encode
from rest_framework import status

from hashlib import md5
from Encode.models import ImageData


class ImageApi(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request):
        images = ImageData.objects.all()
        ser = ImageSerializer(images, many= True)
        return JsonResponse(ser.data, safe=False)

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
