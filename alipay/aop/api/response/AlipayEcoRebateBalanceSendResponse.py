#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoRebateBalanceSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoRebateBalanceSendResponse, self).__init__()
        self._jfb_amount = None

    @property
    def jfb_amount(self):
        return self._jfb_amount

    @jfb_amount.setter
    def jfb_amount(self, value):
        self._jfb_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoRebateBalanceSendResponse, self).parse_response_content(response_content)
        if 'jfb_amount' in response:
            self.jfb_amount = response['jfb_amount']
