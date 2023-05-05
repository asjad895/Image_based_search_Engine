from django.shortcuts import render
from app.utils import*
import os
from app.models import Query
import pandas as pd
# Create your views here.
from django.contrib import messages
from django.shortcuts import render
from django.conf import settings
import tensorflow as tf
from django.http import HttpResponse
from tensorflow import keras
from keras.models import Model
from keras.models import load_model
from keras.utils import load_img, img_to_array
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
    return render(request,'result.html')
