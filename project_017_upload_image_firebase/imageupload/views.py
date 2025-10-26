import os

import firebase_admin

from firebase_admin import credentials, storage

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django import forms

from .settings import BASE_DIR, FIREBASE_CREDENTIALS_FILE, FIREBASE_BUCKET_NAME


# Initialize Firebase Admin SDK
cred = credentials.Certificate(
    os.path.join(BASE_DIR, f'credentials/{FIREBASE_CREDENTIALS_FILE}'))
firebase_admin.initialize_app(cred)


class ImageUploadForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label="Title")
    progress = forms.CharField(widget=forms.Textarea, required=True, label="Description")
    file = forms.FileField(required=True, label="Document Upload")


def check(request):
    form = ImageUploadForm()
    return render(request, "check.html", {"form": form})


def postcreate(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            progress = form.cleaned_data['progress']
            file = form.cleaned_data['file']

            # Upload file to Firebase Storage
            bucket = storage.bucket(FIREBASE_BUCKET_NAME)
            blob = bucket.blob(file.name)
            blob.metadata = {
                "title": title,
                "description": progress
            }
            blob.upload_from_file(file, content_type=file.content_type)

            return render(request, "success.html")
    else:
        form = ImageUploadForm()
    return render(request, "check.html", {"form": form})


def display_data(request):
    bucket = storage.bucket(FIREBASE_BUCKET_NAME)
    blobs = bucket.list_blobs()

    data = []
    for blob in blobs:
        print(blob)
        print(blob.name)
        
        # Assuming metadata contains title and description
        metadata = blob.metadata or {}
        data.append({
            "image_url": blob.public_url,
            "image_name": blob.name,
            "title": metadata.get("title", "No Title"),
            "description": metadata.get("description", "No Description")
        })

    return render(request, "data_display.html", {"data": data})

