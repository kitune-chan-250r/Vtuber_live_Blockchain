from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

urlpatterns = [
    path('transaction/', TransactionView.as_view()),#vtuber 全件取得
    path('minig/', MinigView.as_view()),
    path('fullchain/', FullChainView.as_view())
    #path('mining', MiningView.as_view()),
    #path('chain', ChainView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)