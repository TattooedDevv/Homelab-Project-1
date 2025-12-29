from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def home(request):
    return Response({"message": "Backend is running. Try /api/health/"})

@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})

from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Backend is running. Try /api/health/"})


