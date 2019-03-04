#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeNormalpayOrderDisburseResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeNormalpayOrderDisburseResponse, self).__init__()
        self._operate_no = None
        self._request_accept_time = None
        self._request_no = None
        self._retry = None

    @property
    def operate_no(self):
        return self._operate_no

    @operate_no.setter
    def operate_no(self, value):
        self._operate_no = value
    @property
    def request_accept_time(self):
        return self._request_accept_time

    @request_accept_time.setter
    def request_accept_time(self, value):
        self._request_accept_time = value
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
        response = super(MybankPaymentTradeNormalpayOrderDisburseResponse, self).parse_response_content(response_content)
        if 'operate_no' in response:
            self.operate_no = response['operate_no']
        if 'request_accept_time' in response:
            self.request_accept_time = response['request_accept_time']
        if 'request_no' in response:
            self.request_no = response['request_no']
        if 'retry' in response:
            self.retry = response['retry']
