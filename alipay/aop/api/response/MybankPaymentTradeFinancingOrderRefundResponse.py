#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeFinancingOrderRefundResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeFinancingOrderRefundResponse, self).__init__()
        self._biz_sts = None
        self._operate_no = None
        self._request_accept_time = None
        self._request_no = None

    @property
    def biz_sts(self):
        return self._biz_sts

    @biz_sts.setter
    def biz_sts(self, value):
        self._biz_sts = value
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

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeFinancingOrderRefundResponse, self).parse_response_content(response_content)
        if 'biz_sts' in response:
            self.biz_sts = response['biz_sts']
        if 'operate_no' in response:
            self.operate_no = response['operate_no']
        if 'request_accept_time' in response:
            self.request_accept_time = response['request_accept_time']
        if 'request_no' in response:
            self.request_no = response['request_no']
