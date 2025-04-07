#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflinePaysaasOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflinePaysaasOrderQueryResponse, self).__init__()
        self._isv_order_no = None
        self._order_status = None
        self._pay_time = None

    @property
    def isv_order_no(self):
        return self._isv_order_no

    @isv_order_no.setter
    def isv_order_no(self, value):
        self._isv_order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflinePaysaasOrderQueryResponse, self).parse_response_content(response_content)
        if 'isv_order_no' in response:
            self.isv_order_no = response['isv_order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
