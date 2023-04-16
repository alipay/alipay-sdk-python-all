#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniOrderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderRefundResponse, self).__init__()
        self._refund_id = None
        self._send_back_fee = None

    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, value):
        self._refund_id = value
    @property
    def send_back_fee(self):
        return self._send_back_fee

    @send_back_fee.setter
    def send_back_fee(self, value):
        self._send_back_fee = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderRefundResponse, self).parse_response_content(response_content)
        if 'refund_id' in response:
            self.refund_id = response['refund_id']
        if 'send_back_fee' in response:
            self.send_back_fee = response['send_back_fee']
