#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandActivityQualificationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandActivityQualificationQueryResponse, self).__init__()
        self._detail_msg = None
        self._error_code = None
        self._has_qualification = None

    @property
    def detail_msg(self):
        return self._detail_msg

    @detail_msg.setter
    def detail_msg(self, value):
        self._detail_msg = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def has_qualification(self):
        return self._has_qualification

    @has_qualification.setter
    def has_qualification(self, value):
        self._has_qualification = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandActivityQualificationQueryResponse, self).parse_response_content(response_content)
        if 'detail_msg' in response:
            self.detail_msg = response['detail_msg']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'has_qualification' in response:
            self.has_qualification = response['has_qualification']
