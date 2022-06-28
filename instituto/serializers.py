# from rest_framework import serializers
# from .models import Users


# class UsersSerializer(serializers.Serializer):
#     codigo = serializers.IntegerField(read_only=True)
#     descripcion = serializers.CharField()
#     precio = serializers.DecimalField(max_digits=5, decimal_places=2)
#     imagen = serializers.CharField()
#     class Meta:
#         model = Users
#         fields = ('codigo', 'descripcion', 'precio','imagen')

#     def create(self, validated_data):
#         """
#         Create and return a new `Serie` instance, given the validated data.
#         """
#         return Producto.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Serie` instance, given the validated data.
#         """
#         instance.codigo = validated_data.get('codigo', instance.codigo)
#         instance.descripcion= validated_data.get('descripcion', instance.descripcion)
#         instance.precio= validated_data.get('precio', instance.precio)
#         instance.imagen= validated_data.get('imagen', instance.imagen)
#         instance.save()
#         return instance

# class ProductoSerializer(serializers.ModelSerializer):
#      class Meta:
#          model = Producto
#          fields = ('codigo', 'descripcion', 'precio','imagen')