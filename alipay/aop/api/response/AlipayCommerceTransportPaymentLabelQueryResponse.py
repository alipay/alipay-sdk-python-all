#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportPaymentLabelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportPaymentLabelQueryResponse, self).__init__()
        self._is_hit = None

    @property
    def is_hit(self):
        return self._is_hit

    @is_hit.setter
    def is_hit(self, value):
        self._is_hit = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportPaymentLabelQueryResponse, self).parse_response_content(response_content)
        if 'is_hit' in response:
            self.is_hit = response['is_hit']
