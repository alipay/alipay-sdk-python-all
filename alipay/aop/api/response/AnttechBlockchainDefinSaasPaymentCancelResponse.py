#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinSaasPaymentCancelResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinSaasPaymentCancelResponse, self).__init__()
        self._available_amount = None
        self._available_currency = None
        self._fund_mode = None
        self._order_state = None
        self._out_order_id = None
        self._out_request_id = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def available_currency(self):
        return self._available_currency

    @available_currency.setter
    def available_currency(self, value):
        self._available_currency = value
    @property
    def fund_mode(self):
        return self._fund_mode

    @fund_mode.setter
    def fund_mode(self, value):
        self._fund_mode = value
    @property
    def order_state(self):
        return self._order_state

    @order_state.setter
    def order_state(self, value):
        self._order_state = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_request_id(self):
        return self._out_request_id

    @out_request_id.setter
    def out_request_id(self, value):
        self._out_request_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinSaasPaymentCancelResponse, self).parse_response_content(response_content)
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'available_currency' in response:
            self.available_currency = response['available_currency']
        if 'fund_mode' in response:
            self.fund_mode = response['fund_mode']
        if 'order_state' in response:
            self.order_state = response['order_state']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'out_request_id' in response:
            self.out_request_id = response['out_request_id']
