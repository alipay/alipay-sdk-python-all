#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEmployeeIdlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEmployeeIdlistQueryResponse, self).__init__()
        self._current_page = None
        self._employee_id_list = None
        self._total_num = None
        self._total_pages = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def employee_id_list(self):
        return self._employee_id_list

    @employee_id_list.setter
    def employee_id_list(self, value):
        if isinstance(value, list):
            self._employee_id_list = list()
            for i in value:
                self._employee_id_list.append(i)
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEmployeeIdlistQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'employee_id_list' in response:
            self.employee_id_list = response['employee_id_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
