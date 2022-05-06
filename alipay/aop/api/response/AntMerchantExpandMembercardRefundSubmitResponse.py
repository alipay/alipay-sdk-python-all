#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandMembercardRefundSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandMembercardRefundSubmitResponse, self).__init__()
        self._refund_amount = None
        self._refund_fee = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandMembercardRefundSubmitResponse, self).parse_response_content(response_content)
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_fee' in response:
            self.refund_fee = response['refund_fee']
