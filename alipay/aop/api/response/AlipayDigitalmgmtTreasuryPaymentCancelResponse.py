#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtTreasuryPaymentCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtTreasuryPaymentCancelResponse, self).__init__()
        self._payment_cancel_success = None

    @property
    def payment_cancel_success(self):
        return self._payment_cancel_success

    @payment_cancel_success.setter
    def payment_cancel_success(self, value):
        self._payment_cancel_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtTreasuryPaymentCancelResponse, self).parse_response_content(response_content)
        if 'payment_cancel_success' in response:
            self.payment_cancel_success = response['payment_cancel_success']
