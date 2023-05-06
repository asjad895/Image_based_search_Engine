from django.shortcuts import render
from app.utils import*
import os
from app.models import Query
import pandas as pd
# Create your views here.
from django.contrib import messages
from django.shortcuts import render
from django.conf import settings


def search(request):
    if request.method == 'POST' and request.FILES['query_image']:
        # Load the query image
        query_image = request.FILES['query_image']
        k = request.GET.get('k')
        q = Query.objects.create(image=query_image,k=k)
        print(query_image)
        import requests

# Set the URL of your deployed Streamlit app
        url = 'https://your-streamlit-app-url/predict_endpoint'

# Set the image file path
        image_path = 'path/to/your/image.jpg'

# Open the image file and read its contents as binary data
        with open(image_path, 'rb') as f:
             image_data = f.read()

# Set the request headers
        headers = {'Content-Type': 'application/octet-stream'}

# Set the request data
        data = {'image': image_data}

# Make the prediction request
        response = requests.post(url, headers=headers, data=data)

# Get the prediction from the response
        prediction = response.json()

        # Render the template
        messages.success(request,{'query_image': query_image, 'retrieved_paths': rt})
        return render(request, 'result.html', {'query_image': query_image, 'retrieved_paths': rt})
    else:
        return render(request, 'index.html')

def results(request):
    return render(request,'result.html')
