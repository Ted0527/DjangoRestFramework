from rest_framework import serializers
from watchlist_app.models import StreamPlatform, Watchlist, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
    
class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Watchlist
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # models.py 의 클래스 명 소문자 형태
    # watchlist = serializers.StringRelatedField(many=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'
        

# class MovieSerializer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Movie
#         fields = '__all__'

#     def get_len_name(self, data):
#         return len(data.name)

#     def validate(self, data): 
# # ModelSerializer 를 사용할때 validator 를 따로 추가해줘야 한다.(중요)
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Error')
#         else:
#             return data

#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("short error")
#         else:
#             return value

## serializers.Serializer ##
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance