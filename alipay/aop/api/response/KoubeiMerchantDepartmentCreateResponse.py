#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMerchantDepartmentCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantDepartmentCreateResponse, self).__init__()
        self._dept_id = None

    @property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantDepartmentCreateResponse, self).parse_response_content(response_content)
        if 'dept_id' in response:
            self.dept_id = response['dept_id']
