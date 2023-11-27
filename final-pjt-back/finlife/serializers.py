from rest_framework import serializers
from .models import *



# 예금 옵션리스트 뽑아오는 시리얼라이저
class DepositOptionslistSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'


# 예금 개별 상품 옵션
class DepositOptionsSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    depositoptions_set = DepositOptionslistSerializer(many=True, read_only=True)
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)


# 예금 상품 + 그 상품 옵션까지
class DepositProductsSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    depositoptions_set = DepositOptionslistSerializer(many=True, read_only=True)
    class Meta:
        model = DepositProduct
        fields = '__all__'


# 적금 옵션리스트 뽑아오는 시리얼라이저
class SavingOptionslistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'


# 적금 상품 + 그 상품 옵션까지한꺼번에
class SavingProductsSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    savingoptions_set = SavingOptionslistSerializer(many=True, read_only=True)
    class Meta:
        model = SavingProduct
        fields = '__all__'


# 적금 개별 상품 옵션 
class SavingOptionsSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    savingoptions_set = SavingOptionslistSerializer(many=True, read_only=True)
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)


# 예금 상품 이름만 뽑아올 시리얼라이저
class SelectDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = ('fin_prdt_nm',)

# 적금 상품 이름만 뽑아올 시리얼라이저
class SelectSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = ('fin_prdt_nm',)