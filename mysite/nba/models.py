from django.db import models
from django.db.models import Q
from model_utils import Choices

ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'post_time')
)
class News(models.Model):
    title=models.CharField(max_length=255)
    content = models.TextField(blank=True)
    img_url = models.URLField(blank=True)
    url=models.URLField(blank=True)
    author=models.CharField(max_length=255)
    post_time=models.DateTimeField()
    pre_content=models.TextField(blank=True)

    class Meta:

        db_table = "nba_news"
# Create your models here.


def query_nba_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = News.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(title__icontains=search_value) |
                                   Q(pre_content__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }
