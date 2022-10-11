from rest_framework.pagination import PageNumberPagination

class IQoutesPagination(PageNumberPagination):
    page_size = 1
