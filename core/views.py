from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
# Create your views here.
class PostListAPIView(APIView):
    def get(self, request, format=None):
        r=requests.get("https://jsonplaceholder.typicode.com/posts")
        json_data = r.json()
        return Response(json_data)

class PostDetailAPIView(APIView):
    def get(self, request, post_id, format=None):
        r=requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/")
        json_data = r.json()
        return Response(json_data)