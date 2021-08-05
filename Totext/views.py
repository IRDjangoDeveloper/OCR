from django.http import JsonResponse
from django.shortcuts import render
# import pytesseract to convert text in image to string
import pytesseract
from .forms import imageForm, textinput
import os
# import Image from PIL to read image
from PIL import Image
from django.conf import settings
from .models import ImageUploadModel

# Create your views here.
def ImageToText(request):
    text = ''
    form = imageForm(request.POST, request.FILES)
    if request.is_ajax():
        if request.method == 'POST':
            if form.is_valid():
                lang = form.cleaned_data.get('lang')
                image = request.FILES['img']
                image1 = ImageUploadModel.objects.create(image=image)
                mediapath = settings.MEDIA_ROOT
                path = '{}/{}'.format(mediapath , image1.image)
                text = pytesseract.image_to_string(Image.open(path), lang=lang)
                print(text)
                os.remove(path)
                return JsonResponse({'ok': lang, 'text':text})
    return render(request, 'index.html', {'form':form, 'text':text, 'textinput':textinput})