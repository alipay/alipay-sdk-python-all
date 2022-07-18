#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcDepartmentSublistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcDepartmentSublistQueryResponse, self).__init__()
        self._department_id_list = None

    @property
    def department_id_list(self):
        return self._department_id_list

    @department_id_list.setter
    def department_id_list(self, value):
        if isinstance(value, list):
            self._department_id_list = list()
            for i in value:
                self._department_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcDepartmentSublistQueryResponse, self).parse_response_content(response_content)
        if 'department_id_list' in response:
            self.department_id_list = response['department_id_list']
