#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsRightsOrderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsRightsOrderRefundResponse, self).__init__()
        self._refund_valid = None

    @property
    def refund_valid(self):
        return self._refund_valid

    @refund_valid.setter
    def refund_valid(self, value):
        self._refund_valid = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsRightsOrderRefundResponse, self).parse_response_content(response_content)
        if 'refund_valid' in response:
            self.refund_valid = response['refund_valid']
