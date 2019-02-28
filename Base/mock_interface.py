# -*- coding: utf-8 -*-

from mock import mock


def mock_test(mock_method, url, method, request_data, response_data):
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url, method, request_data)
    return res
