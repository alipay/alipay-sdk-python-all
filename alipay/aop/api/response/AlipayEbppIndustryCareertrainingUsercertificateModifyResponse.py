#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryCareertrainingUsercertificateModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCareertrainingUsercertificateModifyResponse, self).__init__()
        self._biz_code = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCareertrainingUsercertificateModifyResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
