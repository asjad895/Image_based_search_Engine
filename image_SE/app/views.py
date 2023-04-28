from django.shortcuts import render
from app.utils import*
import os
from app.models import Query
import pandas as pd
# Create your views here.
from django.contrib import messages
from django.shortcuts import render
from django.conf import settings
import tensorflow
from django.http import HttpResponse
import tensorflow.keras
from keras.models import Model
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import csv
import numpy as np

def search(request):
    if request.method == 'POST' and request.FILES['query_image']:
        # Load the query image
        query_image = request.FILES['query_image']
        k = request.GET.get('k')
        q = Query.objects.create(image=query_image,k=k)
        print(query_image)
        d,rt,cap=retrived(query_image)
        # Render the template
        messages.success(request,{'query_image': query_image, 'retrieved_paths': rt})
        return render(request, 'result.html', {'query_image': query_image, 'retrieved_paths': rt})
    else:
        return render(request, 'index.html')

def results(request):
    image_path = os.path.join(settings.MEDIA_ROOT, 'upload', '1000268201_693b08cb0e.jpg')
    print(image_path)
    with open(image_path, 'rb') as f:
        # return HttpResponse(f.read(), content_type='image/jpeg')
        img=f.read()
    d={'img':img}
    return render(request,'result.html',d)
