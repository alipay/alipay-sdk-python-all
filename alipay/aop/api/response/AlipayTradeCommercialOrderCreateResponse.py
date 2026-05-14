#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCommercialOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCommercialOrderCreateResponse, self).__init__()
        self._checkout_url = None
        self._order_no = None
        self._status = None

    @property
    def checkout_url(self):
        return self._checkout_url

    @checkout_url.setter
    def checkout_url(self, value):
        self._checkout_url = value
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
        response = super(AlipayTradeCommercialOrderCreateResponse, self).parse_response_content(response_content)
        if 'checkout_url' in response:
            self.checkout_url = response['checkout_url']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'status' in response:
            self.status = response['status']
