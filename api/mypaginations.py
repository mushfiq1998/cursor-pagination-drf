from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    # Three records will be shown per page
    page_size = 2

    # Ordering the records based on name field
    ordering = 'name'

    # Define custom cursor_query_param
    # We know that default cursor_query_param is 'cursor'
    cursor_query_param = 'cu'
