#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinSaasPaymentCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinSaasPaymentCreateResponse, self).__init__()
        self._fund_mode = None
        self._order_state = None
        self._out_order_id = None
        self._out_payee_id = None
        self._out_payer_id = None
        self._platform_member_id = None

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
    def out_payee_id(self):
        return self._out_payee_id

    @out_payee_id.setter
    def out_payee_id(self, value):
        self._out_payee_id = value
    @property
    def out_payer_id(self):
        return self._out_payer_id

    @out_payer_id.setter
    def out_payer_id(self, value):
        self._out_payer_id = value
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinSaasPaymentCreateResponse, self).parse_response_content(response_content)
        if 'fund_mode' in response:
            self.fund_mode = response['fund_mode']
        if 'order_state' in response:
            self.order_state = response['order_state']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'out_payee_id' in response:
            self.out_payee_id = response['out_payee_id']
        if 'out_payer_id' in response:
            self.out_payer_id = response['out_payer_id']
        if 'platform_member_id' in response:
            self.platform_member_id = response['platform_member_id']
