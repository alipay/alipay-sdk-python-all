#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTourVoucherRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTourVoucherRefundResponse, self).__init__()
        self._out_refund_id = None
        self._refund_amount = None

    @property
    def out_refund_id(self):
        return self._out_refund_id

    @out_refund_id.setter
    def out_refund_id(self, value):
        self._out_refund_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTourVoucherRefundResponse, self).parse_response_content(response_content)
        if 'out_refund_id' in response:
            self.out_refund_id = response['out_refund_id']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
