from rest_framework import views
from rest_framework.response import Response
from .services import get_methods_list, get_method_details, call_method


class MethodAPIView(views.APIView):

    def get(self, request) -> Response:
        methods_list = get_methods_list()
        return Response({'methods': methods_list})

    def post(self, request) -> Response:
        data = request.data
        method = data.get('method')
        data.pop('method', None)
        response = call_method(method, data)
        return Response({"method": method, "response": response})


class MethodDetailAPIView(views.APIView):

    def get(self, request, method) -> Response:
        method_params = get_method_details(method)
        return Response({'method': method, 'parameters': method_params})


