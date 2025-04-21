#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportChargerRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportChargerRefundQueryResponse, self).__init__()
        self._refund_amount = None
        self._refund_status = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportChargerRefundQueryResponse, self).parse_response_content(response_content)
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
