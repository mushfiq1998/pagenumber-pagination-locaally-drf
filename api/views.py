from .models import Student
from .serializers import StudentSerializer 
from .mypaginations import MyPageNumberPagination
from rest_framework.generics import ListAPIView

class StudentList(ListAPIView): 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination
