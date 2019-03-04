#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeFinancingOrderCloseResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeFinancingOrderCloseResponse, self).__init__()
        self._biz_no = None
        self._biz_sts = None
        self._order_no = None
        self._request_accept_time = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_sts(self):
        return self._biz_sts

    @biz_sts.setter
    def biz_sts(self, value):
        self._biz_sts = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def request_accept_time(self):
        return self._request_accept_time

    @request_accept_time.setter
    def request_accept_time(self, value):
        self._request_accept_time = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeFinancingOrderCloseResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'biz_sts' in response:
            self.biz_sts = response['biz_sts']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'request_accept_time' in response:
            self.request_accept_time = response['request_accept_time']
