#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryRentOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryRentOrderCreateResponse, self).__init__()
        self._biz_seq = None
        self._order_status = None
        self._pay_url = None

    @property
    def biz_seq(self):
        return self._biz_seq

    @biz_seq.setter
    def biz_seq(self, value):
        self._biz_seq = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryRentOrderCreateResponse, self).parse_response_content(response_content)
        if 'biz_seq' in response:
            self.biz_seq = response['biz_seq']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'pay_url' in response:
            self.pay_url = response['pay_url']
