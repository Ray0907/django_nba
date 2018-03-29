from nba.models import News
from nba.serializers import NewsSerializer
from django.template.response import TemplateResponse
from django.http.response import HttpResponse
from rest_framework import viewsets,status
from django.shortcuts import render
from rest_framework.response import Response
from .models import query_nba_by_args

def home(request):
    news_list = News.objects.all()
    return render(request, 'index.html', {
        'news_list': news_list,
    })
# Create your views here.


def index(request):
    html = TemplateResponse(request, 'home.html')
    return HttpResponse(html.render())


def news_detail(request,id):
    detail = News.objects.get(id=id)
    return render(request, 'detail.html', {
        'detail': detail
    })
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def list(self, request, **kwargs):
        try:
            nba = query_nba_by_args(**request.query_params)
            serializer = NewsSerializer(nba['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = nba['draw'] if "draw" in nba else None
            result['recordsTotal'] = nba['total'] if "total" in nba else None
            result['recordsFiltered'] = nba['count'] if "count" in nba else None
            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)



