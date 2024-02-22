from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer

class FeedSerializer(ModelSerializer):
    user = FeedUserSerializer(read_only=True)
    # 역참조 헤서 review를 가져온다
    review_set = ReviewSerializer(many=True,read_only=True)
    class Meta:
        # feed이라는 모델에 있는  fiedls들 모두 직렬화
        model = Feed
        fields ="__all__"
        depth = 1