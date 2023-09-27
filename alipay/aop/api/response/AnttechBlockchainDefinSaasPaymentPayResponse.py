#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccountDTO import AccountDTO


class AnttechBlockchainDefinSaasPaymentPayResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinSaasPaymentPayResponse, self).__init__()
        self._fund_mode = None
        self._order_state = None
        self._out_order_id = None
        self._payee_account = None
        self._payment_error_message = None
        self._platform_member_id = None
        self._state = None

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
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        if isinstance(value, AccountDTO):
            self._payee_account = value
        else:
            self._payee_account = AccountDTO.from_alipay_dict(value)
    @property
    def payment_error_message(self):
        return self._payment_error_message

    @payment_error_message.setter
    def payment_error_message(self, value):
        self._payment_error_message = value
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinSaasPaymentPayResponse, self).parse_response_content(response_content)
        if 'fund_mode' in response:
            self.fund_mode = response['fund_mode']
        if 'order_state' in response:
            self.order_state = response['order_state']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'payee_account' in response:
            self.payee_account = response['payee_account']
        if 'payment_error_message' in response:
            self.payment_error_message = response['payment_error_message']
        if 'platform_member_id' in response:
            self.platform_member_id = response['platform_member_id']
        if 'state' in response:
            self.state = response['state']
