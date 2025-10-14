#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntiepLinkedmallenergyConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntiepLinkedmallenergyConsultResponse, self).__init__()
        self._allow = None
        self._biz_desc = None
        self._biz_result_code = None
        self._biz_success = None

    @property
    def allow(self):
        return self._allow

    @allow.setter
    def allow(self, value):
        self._allow = value
    @property
    def biz_desc(self):
        return self._biz_desc

    @biz_desc.setter
    def biz_desc(self, value):
        self._biz_desc = value
    @property
    def biz_result_code(self):
        return self._biz_result_code

    @biz_result_code.setter
    def biz_result_code(self, value):
        self._biz_result_code = value
    @property
    def biz_success(self):
        return self._biz_success

    @biz_success.setter
    def biz_success(self, value):
        self._biz_success = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntiepLinkedmallenergyConsultResponse, self).parse_response_content(response_content)
        if 'allow' in response:
            self.allow = response['allow']
        if 'biz_desc' in response:
            self.biz_desc = response['biz_desc']
        if 'biz_result_code' in response:
            self.biz_result_code = response['biz_result_code']
        if 'biz_success' in response:
            self.biz_success = response['biz_success']
