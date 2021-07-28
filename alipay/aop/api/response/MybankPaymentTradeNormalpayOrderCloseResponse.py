#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeNormalpayOrderCloseResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeNormalpayOrderCloseResponse, self).__init__()
        self._order_no = None
        self._request_no = None
        self._retry = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeNormalpayOrderCloseResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'request_no' in response:
            self.request_no = response['request_no']
        if 'retry' in response:
            self.retry = response['retry']
