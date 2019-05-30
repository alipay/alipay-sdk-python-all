#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeIndustryOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeIndustryOrderQueryResponse, self).__init__()
        self._out_order_no = None
        self._status = None
        self._zm_order_id = None

    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def zm_order_id(self):
        return self._zm_order_id

    @zm_order_id.setter
    def zm_order_id(self, value):
        self._zm_order_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeIndustryOrderQueryResponse, self).parse_response_content(response_content)
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'status' in response:
            self.status = response['status']
        if 'zm_order_id' in response:
            self.zm_order_id = response['zm_order_id']
