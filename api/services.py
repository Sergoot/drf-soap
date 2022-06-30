import os
from django.http import Http404
from zeep import Client, helpers, exceptions


def get_methods_list() -> list:
    """ Вовзращает список доступных методов сервиса """
    client = Client(os.environ.get('WSDL'))
    return [a[0] for a in client.service]


def get_method_details(method: str) -> dict:
    """ Возвращает словарь с параметрами данного метода """
    parameters = {}
    client = Client(os.environ.get('WSDL'))
    try:
        method_type = client.get_type(f'ns0:{method}')
    except exceptions.LookupError:
        raise Http404
    for elem in method_type.elements:
        parameters.update({elem[0]: elem[1].type.name})
    return parameters


def call_method(method: str, params: dict) -> list:
    """ Возвращает результат вызова метода """
    client = Client(os.environ.get('WSDL'))
    try:
        response = client.service.__getattr__(method)(**params)
    except AttributeError:
        raise Http404
    return helpers.serialize_object(response)
