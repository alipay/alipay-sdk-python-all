#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationTimescardRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationTimescardRefundQueryResponse, self).__init__()
        self._refundable_amount = None

    @property
    def refundable_amount(self):
        return self._refundable_amount

    @refundable_amount.setter
    def refundable_amount(self, value):
        self._refundable_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationTimescardRefundQueryResponse, self).parse_response_content(response_content)
        if 'refundable_amount' in response:
            self.refundable_amount = response['refundable_amount']
