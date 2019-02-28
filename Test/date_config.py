# -*- coding: utf-8 -*-


class global_var:

    # case id
    Id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    date_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'


# 获取case id
def get_id():
    return global_var.Id


# 获取url
def get_urrl():
    return global_var.url


# 获取是否执行
def get_run():
    return global_var.run


# 获取请求方式
def get_request_way():
    return global_var.request_way


# 获取是否携带header
def get_header():
    return global_var.header


# 获取header值
def get_header_value():
    header = {
        "header":"1234",
        "cookie":"test"
    }
    return header


# 获取依赖id
def get_case_depend():
    return global_var.case_depend


# 获取依赖数据
def get_data_depend():
    return global_var.date_depend


# 获取依赖数据字段
def get_field_depend():
    return global_var.field_depend


# 获取请求数据
def get_data():
    return global_var.data


# 获取预期结果
def get_expect():
    return global_var.expect


# 获取实际结果
def get_result():
    return global_var.result
