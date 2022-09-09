#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcDepartmentCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcDepartmentCreateResponse, self).__init__()
        self._department_id = None

    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcDepartmentCreateResponse, self).parse_response_content(response_content)
        if 'department_id' in response:
            self.department_id = response['department_id']
