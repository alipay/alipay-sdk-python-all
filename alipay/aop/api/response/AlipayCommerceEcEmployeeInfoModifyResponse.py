#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEmployeeInfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEmployeeInfoModifyResponse, self).__init__()
        self._employee_id = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEmployeeInfoModifyResponse, self).parse_response_content(response_content)
        if 'employee_id' in response:
            self.employee_id = response['employee_id']
