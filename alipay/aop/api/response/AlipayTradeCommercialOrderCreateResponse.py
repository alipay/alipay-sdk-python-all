#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCommercialOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCommercialOrderCreateResponse, self).__init__()
        self._alipay_jump_schema = None
        self._alipay_schema = None
        self._checkout_url = None
        self._order_no = None
        self._qr_code = None
        self._status = None

    @property
    def alipay_jump_schema(self):
        return self._alipay_jump_schema

    @alipay_jump_schema.setter
    def alipay_jump_schema(self, value):
        self._alipay_jump_schema = value
    @property
    def alipay_schema(self):
        return self._alipay_schema

    @alipay_schema.setter
    def alipay_schema(self, value):
        self._alipay_schema = value
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
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCommercialOrderCreateResponse, self).parse_response_content(response_content)
        if 'alipay_jump_schema' in response:
            self.alipay_jump_schema = response['alipay_jump_schema']
        if 'alipay_schema' in response:
            self.alipay_schema = response['alipay_schema']
        if 'checkout_url' in response:
            self.checkout_url = response['checkout_url']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'qr_code' in response:
            self.qr_code = response['qr_code']
        if 'status' in response:
            self.status = response['status']
