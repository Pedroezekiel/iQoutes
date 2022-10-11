from . import pagination
from .models import Quotes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json
import requests

class GenerateQuote(APIView):
    queryset = Quotes.objects.filter()


    def get(self, request, format=None):
        results = self.request.query_params.get('text')
        response = {}

        r = requests.get(
            'https://goquotes-api.herokuapp.com/api/v1/random?count=10')

        r_status = 200

        if r_status == 200:

            data = r.json()
            quotes = data['quotes']

            for q in quotes:
                quote = Quotes(
                    text=q['text'],
                    author=q['author']
                )
                pagination_class = pagination.IQoutesPagination
                quote.save()
                
                # paginator = Paginator(quotes, 1)
                # page = requests.get('page')
                # try:
                #     posts = Paginator.page(page)
                # except PageNotAnInteger:
                #     posts = Paginator.page(1)
                # except EmptyPage:
                #     posts = Paginator.page(Paginator.num_pages)
                # all_qoutes = Quote.objects.all().order_by('-id')
            response['status'] = 200
            response['message'] = 'success'
            response['count'] = data

        else:
            response['status'] = 200
            response['message'] = 'error'
            response['credentials'] = {}

        return Response(response)
