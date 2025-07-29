#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducatePlaceInfoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducatePlaceInfoCreateResponse, self).__init__()
        self._not_exist_employee_no_list = None
        self._place_id = None

    @property
    def not_exist_employee_no_list(self):
        return self._not_exist_employee_no_list

    @not_exist_employee_no_list.setter
    def not_exist_employee_no_list(self, value):
        if isinstance(value, list):
            self._not_exist_employee_no_list = list()
            for i in value:
                self._not_exist_employee_no_list.append(i)
    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        self._place_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducatePlaceInfoCreateResponse, self).parse_response_content(response_content)
        if 'not_exist_employee_no_list' in response:
            self.not_exist_employee_no_list = response['not_exist_employee_no_list']
        if 'place_id' in response:
            self.place_id = response['place_id']
