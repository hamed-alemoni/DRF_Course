from rest_framework.viewsets import ModelViewSet
from .serializers import ArticleSerializer, UserSerializer
from blog.models import Article
from .permissions import IsSuperuserOrAuthorReadOnly, IsStaffOrReadOnly, IsAuthorOrReadOnly
from django.contrib.auth import get_user_model


# Create your views here.
######## second way instead of viewsets(Article) ######

# a view to make all objects info serialize
# get objects
# create new object
# class ArticleList(ListCreateAPIView):
#     # get all articles
#     queryset = Article.objects.all()
#     # determine serializer class
#     serializer_class = ArticleSerializer
#     # add a new permission for this view
#     permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)

# a view to make an object info serialize
# retrieve object
# update object
# destroy object
# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     # get all articles
#     queryset = Article.objects.all()
#     # determine serializer class
#     serializer_class = ArticleSerializer
#     # add a new permission for this view
#     permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class ArticleViewSet(ModelViewSet):
    # get all articles
    queryset = Article.objects.all()
    # determine serializer class
    serializer_class = ArticleSerializer
    # determine filtering fields
    filterset_fields = ['status', 'author__username']
    # determine ordering fields
    ordering_fields = ['status', 'publish']
    # default ordering
    ordering = ['-publish']
    # determine search fields
    search_fields = [

        'title',
        'content',
        'author__username',
        'author__first_name',
        'author__last_name',

    ]

    # add a new permission for this view
    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = (IsStaffOrReadOnly,)
        else:
            permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)
        return [permission() for permission in permission_classes]

        ######## second way instead of viewsets(User) ######


# a view to make all objects info serialize
# get objects
# create new object
# class UserList(ListCreateAPIView):
#     # get all articles
#     queryset = User.objects.all()
#     # determine serializer class
#     serializer_class = UserSerializer
#     # add a new permission for this view
#     permission_classes = (IsSuperuserOrAuthorReadOnly,)


# a view to make an object info serialize
# retrieve object
# update object
# destroy object
# class UserDetail(RetrieveUpdateDestroyAPIView):
#     # get all articles
#     queryset = User.objects.all()
#     # determine serializer class
#     serializer_class = UserSerializer
#     # add a new permission for this view
#     permission_classes = (IsSuperuserOrAuthorReadOnly,)


class UserViewSet(ModelViewSet):
    # get all articles
    queryset = get_user_model().objects.all()
    # determine serializer class
    serializer_class = UserSerializer
    # add a new permission for this view
    permission_classes = (IsSuperuserOrAuthorReadOnly,)

