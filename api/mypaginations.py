from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 2

    # Default page query param is 'page'
    # Set custom page query param
    page_query_param = 'p'

    # Set page size by client
    # Here, 'records' is a normal variable 
    page_size_query_param = 'records'

    # Define maximum page size
    # Client can not show more than 7 records in a single page
    max_page_size = 7

    # Chabge default 'last' attribute to any other
    last_page_strings = 'end'
