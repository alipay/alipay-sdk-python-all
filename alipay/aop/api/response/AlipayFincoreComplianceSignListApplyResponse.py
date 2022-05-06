#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFincoreComplianceSignListApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceSignListApplyResponse, self).__init__()
        self._business_id = None
        self._file_code = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def file_code(self):
        return self._file_code

    @file_code.setter
    def file_code(self, value):
        self._file_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceSignListApplyResponse, self).parse_response_content(response_content)
        if 'business_id' in response:
            self.business_id = response['business_id']
        if 'file_code' in response:
            self.file_code = response['file_code']
