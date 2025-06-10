#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowFundtradeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowFundtradeCreateResponse, self).__init__()
        self._biz_no = None
        self._order_pay_url = None
        self._status = None
        self._trade_no = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def order_pay_url(self):
        return self._order_pay_url

    @order_pay_url.setter
    def order_pay_url(self, value):
        self._order_pay_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowFundtradeCreateResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'order_pay_url' in response:
            self.order_pay_url = response['order_pay_url']
        if 'status' in response:
            self.status = response['status']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
