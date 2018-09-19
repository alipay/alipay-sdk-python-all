#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskAntifraudVerifyResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskAntifraudVerifyResponse, self).__init__()
        self._biz_no = None
        self._unique_id = None
        self._verify_code = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value
    @property
    def verify_code(self):
        return self._verify_code

    @verify_code.setter
    def verify_code(self, value):
        self._verify_code = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskAntifraudVerifyResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
        if 'verify_code' in response:
            self.verify_code = response['verify_code']
