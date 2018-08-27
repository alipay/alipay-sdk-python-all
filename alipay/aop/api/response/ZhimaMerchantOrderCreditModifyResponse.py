#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantOrderCreditModifyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantOrderCreditModifyResponse, self).__init__()
        self._out_order_no = None
        self._overdue_time = None
        self._zm_order_no = None

    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def overdue_time(self):
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, value):
        self._overdue_time = value
    @property
    def zm_order_no(self):
        return self._zm_order_no

    @zm_order_no.setter
    def zm_order_no(self, value):
        self._zm_order_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantOrderCreditModifyResponse, self).parse_response_content(response_content)
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'overdue_time' in response:
            self.overdue_time = response['overdue_time']
        if 'zm_order_no' in response:
            self.zm_order_no = response['zm_order_no']
