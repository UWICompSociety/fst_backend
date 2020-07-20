from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters
from core.models import TestModel
from core.models import Contact
from core.models import Scholarship
from core.models import PhoneNumber
from core.serializers import TestModelSerializer
from core.serializers import ContactSerializer
from core.serializers import ScholarshipSerializer
from core.serializers import PhoneNumberSerializer

# Create your views here.


# def test_view(request):
#     data = {'first_name': 'John', 'last_name': 'Brown'}
#     return JsonResponse(data)


class TestView(APIView):

    def get(self, request, format=None):
        test_models  = TestModel.objects.all()
        serializer  = TestModelSerializer(test_models, many=True)
        return Response(serializer.data)

class ContactView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    ordering_fields = ['id']
    ordering = ['id']
    search_fields = ['name','description','email']

class PhoneNumberView(APIView):

    def get(self, request, format=None):
        phone_num_models = PhoneNumber.objects.all()
        serializer = PhoneNumberSerializer(phone_num_models,many=True)
        return Response(serializer.data)

class ScholarshipView(APIView):

    def get(self, request, format=None):
        scholarship_models = Scholarship.objects.all()
        serializer = ScholarshipSerializer(scholarship_models,many=True)
        return Response(serializer.data)
