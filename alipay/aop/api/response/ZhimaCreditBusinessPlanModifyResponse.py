#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditBusinessPlanModifyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditBusinessPlanModifyResponse, self).__init__()
        self._biz_no = None
        self._out_request_no = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditBusinessPlanModifyResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
