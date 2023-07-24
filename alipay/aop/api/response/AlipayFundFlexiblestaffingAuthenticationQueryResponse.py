#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundFlexiblestaffingAuthenticationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundFlexiblestaffingAuthenticationQueryResponse, self).__init__()
        self._out_biz_no = None
        self._verify_result = None
        self._verify_time = None

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
    @property
    def verify_time(self):
        return self._verify_time

    @verify_time.setter
    def verify_time(self, value):
        self._verify_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundFlexiblestaffingAuthenticationQueryResponse, self).parse_response_content(response_content)
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'verify_result' in response:
            self.verify_result = response['verify_result']
        if 'verify_time' in response:
            self.verify_time = response['verify_time']
