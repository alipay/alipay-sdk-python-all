#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryNucleicacidCodeVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryNucleicacidCodeVerifyResponse, self).__init__()
        self._out_biz_no = None
        self._verify_result = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def verify_result(self):
        return self._verify_result

    @verify_result.setter
    def verify_result(self, value):
        self._verify_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryNucleicacidCodeVerifyResponse, self).parse_response_content(response_content)
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'verify_result' in response:
            self.verify_result = response['verify_result']
