#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcTransAccountTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcTransAccountTransferResponse, self).__init__()
        self._fund_order_id = None
        self._order_no = None
        self._status = None

    @property
    def fund_order_id(self):
        return self._fund_order_id

    @fund_order_id.setter
    def fund_order_id(self, value):
        self._fund_order_id = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcTransAccountTransferResponse, self).parse_response_content(response_content)
        if 'fund_order_id' in response:
            self.fund_order_id = response['fund_order_id']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'status' in response:
            self.status = response['status']
