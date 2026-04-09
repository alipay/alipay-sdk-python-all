#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtTreasuryPaymentAcceptResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtTreasuryPaymentAcceptResponse, self).__init__()
        self._payment_accept_id = None
        self._payment_accept_success = None

    @property
    def payment_accept_id(self):
        return self._payment_accept_id

    @payment_accept_id.setter
    def payment_accept_id(self, value):
        self._payment_accept_id = value
    @property
    def payment_accept_success(self):
        return self._payment_accept_success

    @payment_accept_success.setter
    def payment_accept_success(self, value):
        self._payment_accept_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtTreasuryPaymentAcceptResponse, self).parse_response_content(response_content)
        if 'payment_accept_id' in response:
            self.payment_accept_id = response['payment_accept_id']
        if 'payment_accept_success' in response:
            self.payment_accept_success = response['payment_accept_success']
