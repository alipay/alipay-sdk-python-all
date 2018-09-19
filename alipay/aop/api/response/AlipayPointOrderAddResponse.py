#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPointOrderAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPointOrderAddResponse, self).__init__()
        self._alipay_order_no = None
        self._result_code = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayPointOrderAddResponse, self).parse_response_content(response_content)
        if 'alipay_order_no' in response:
            self.alipay_order_no = response['alipay_order_no']
        if 'result_code' in response:
            self.result_code = response['result_code']
