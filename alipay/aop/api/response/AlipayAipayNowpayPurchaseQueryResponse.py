#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayNowpayPurchaseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayNowpayPurchaseQueryResponse, self).__init__()
        self._purchase_status = None
        self._trade_no = None

    @property
    def purchase_status(self):
        return self._purchase_status

    @purchase_status.setter
    def purchase_status(self, value):
        self._purchase_status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayNowpayPurchaseQueryResponse, self).parse_response_content(response_content)
        if 'purchase_status' in response:
            self.purchase_status = response['purchase_status']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
