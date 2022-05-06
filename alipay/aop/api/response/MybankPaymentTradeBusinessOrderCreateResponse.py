#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeBusinessOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeBusinessOrderCreateResponse, self).__init__()
        self._cashier_url = None
        self._order_no = None
        self._request_no = None
        self._retry = None

    @property
    def cashier_url(self):
        return self._cashier_url

    @cashier_url.setter
    def cashier_url(self, value):
        self._cashier_url = value
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
        response = super(MybankPaymentTradeBusinessOrderCreateResponse, self).parse_response_content(response_content)
        if 'cashier_url' in response:
            self.cashier_url = response['cashier_url']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'request_no' in response:
            self.request_no = response['request_no']
        if 'retry' in response:
            self.retry = response['retry']
