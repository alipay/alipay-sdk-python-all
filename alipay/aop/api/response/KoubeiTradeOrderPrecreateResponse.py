#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiTradeOrderPrecreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeOrderPrecreateResponse, self).__init__()
        self._order_no = None
        self._qr_code = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeOrderPrecreateResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'qr_code' in response:
            self.qr_code = response['qr_code']
