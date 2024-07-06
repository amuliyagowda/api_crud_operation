from django.shortcuts import render
from app.models import *
from rest_framework.views import APIView
from app.serializers import *
from rest_framework.response import Response 

# Create your views here.
class ProductCrud(APIView):
    def get(self,request,pk):
        LPO=Product.objects.all()
        MSPO=ProductMS(LPO,many=True)
        return Response(MSPO.data)
    
    def post(self,request,pk):
        rjd=request.data
        PDO=ProductMS(data=rjd)
        if PDO.is_valid():
            PDO.save()
            return Response({'success':'Data is inserted successfully'})
        else:
            return Response({'Failed':'Issues while inserting'})
        
    def put(self,request,pk):
        rjd=request.data
        instance=Product.objects.get(pk=pk)
        LPO=ProductMS(instance,data=rjd)
        if LPO.is_valid():
            LPO.save()
            return Response({'uodation':'Data updated successfully'})
        else:
            return Response({'Updation':'Updation failed'})
        
    def patch(self,request,pk):
        rjd=request.data
        instance=Product.objects.get(pk=pk)
        LPO=ProductMS(instance,data=rjd,partial=True)
        if LPO.is_valid():
            LPO.save()
            return Response({'Partial update':'Updated successfully'})
        return Response({'Partial update':'updated Failed'})
    

    def delete(self,request,pk):
        instance=Product.objects.get(pk=pk).delete()
