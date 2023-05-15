from rest_framework import serializers
from Web.models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ["id", "name", "price", "description", "category", "image"]
        fields = "__all__"