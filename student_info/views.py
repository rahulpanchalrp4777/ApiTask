
from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from django.core.paginator import Paginator
from .pagination import StandardResultsSetPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

# Create your views here.

@api_view (['GET'])
def student_detail_view(request,id):
    try:
        obj = Student.objects.get(pk = id)
        serializer = StudentSerializer(obj)

        return Response({'payload':serializer.data,'status':200,'message':'successful'}) 
    except:
        return Response({'payload':{},'status':400,'message':'No Data Found'}) 


@api_view(['GET'])
def student_list(request):
    try:
        data = Student.objects.all()
        if len(data)> 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(data, request)
            serializer = StudentSerializer(result_page, many=True)
        # return paginator.get_paginated_response(serializer.data)
        return Response({'payload':serializer.data,'status':200,'message':'successful'})
    except:
        return Response({'payload':{},'status':400,'message':'No Data Found'}) 

class StudentSearchView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['location','technical_skills']



@api_view(["POST"])
def create_student_view(request):
    try:
        print(request.data)
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200,'payload':request.data,'message':'successful'})
        else:
            return Response({'status':400,'message':'there is some problem'})

    except:
        return Response({'status':400,'message':'there is some problem'})

