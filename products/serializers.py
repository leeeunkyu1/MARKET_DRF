from rest_framework import serializers
from .models import Comment, Product


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("Product",)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("product")
        return ret

    

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        
        

class ProductDetailSerializer(ProductSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments = serializers.IntegerField(source="comments.count", read_only=True)