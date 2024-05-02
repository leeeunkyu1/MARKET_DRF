from urllib import request
from django.shortcuts import get_object_or_404, render
from .models import  Product
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Comment
from .serializers import (
    
    CommentSerializer,
    ProductDetailSerializer,
    ProductSerializer,
)


# @api_view(["GET", "POST"])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializers = ArticleSerializer(articles, many=True)
#         return Response(serializers.data)
#     elif request.method == "POST":
#         serializers = ArticleSerializer(data=request.data)
#         if serializers.is_valid(raise_exception=True): #레이지 익셉션은 다음을 대신해줌 return Response(serializers.errors, status=400)
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)

    


class ProductsListAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


class ProductsDetailAPIView(APIView):
    
    
    permission_classes = [IsAuthenticated]
		
    def get_object(self, product_pk):
        return get_object_or_404(Product, pk=product_pk)

    def get(self, request, product_pk):
        article = self.get_object(product_pk)
        serializer = ProductDetailSerializer(Product)
        return Response(serializer.data)

    def put(self, request, product_pk):
        article = self.get_object(product_pk)
        serializer = ProductDetailSerializer(Product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, product_pk):
        article = self.get_object(product_pk)
        article.delete()
        data = {"pk": f"{product_pk} is deleted."}
        return Response(data, status=status.HTTP_200_OK)
    
    
    
    
class CommentListAPIView(APIView):
    
    
    permission_classes = [IsAuthenticated]
    def get(self, request, comments_pk):
        article = get_object_or_404(Product, pk=comments_pk)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, comments_pk):
        article = get_object_or_404(Product, pk=comments_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        

class CommentDetailAPIView(APIView):
    
    
    permission_classes = [IsAuthenticated]
    def get_object(self, comment_pk):
        return get_object_or_404(Comment, pk=comment_pk)

    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        comment.delete()
        data = {"pk": f"{comment_pk} is deleted."}
        return Response(data, status=status.HTTP_200_OK) 