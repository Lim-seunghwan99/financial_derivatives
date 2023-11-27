from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import get_user_model
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, UserSerializer
from .models import Article, Comment


# 회원정보 업데이트
from rest_framework.generics import RetrieveUpdateAPIView
from .permissions import IsOwnerOrReadOnly



@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)    
    
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if request.user == article.user:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        article.delete()
        message = {'message': '게시글이 삭제되었습니다.'}
        return Response(message, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = Comment.objects.filter(article=article)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
    
       
@api_view(['POST'])
def create_comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    data = request.data.copy()  # 요청 데이터 복사
    data['user'] = request.user.id  # 요청한 사용자의 ID를 user 필드에 추가
    data['username'] = request.user.username
    serializer = CommentSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def comments_delete(request, article_pk, comment_pk):
    
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        context = {
            'message' : '댓글이 삭제되었습니다.'
        }
        return Response(context,status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_403_FORBIDDEN)



class UserProfileAPIView(APIView):
    def get(self, request, username):
        userdata = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(userdata)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, username):
        userdata = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(userdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, username):
        userdata = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(userdata, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
