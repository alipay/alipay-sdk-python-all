#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCommercialOrderCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCommercialOrderCloseResponse, self).__init__()
        self._gmt_close = None
        self._order_no = None
        self._status = None
        self._trade_no = None

    @property
    def gmt_close(self):
        return self._gmt_close

    @gmt_close.setter
    def gmt_close(self, value):
        self._gmt_close = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
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
        response = super(AlipayTradeCommercialOrderCloseResponse, self).parse_response_content(response_content)
        if 'gmt_close' in response:
            self.gmt_close = response['gmt_close']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'status' in response:
            self.status = response['status']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
