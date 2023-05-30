#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsOrderInstantdeliveryCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsOrderInstantdeliveryCancelResponse, self).__init__()
        self._cancel_fee = None

    @property
    def cancel_fee(self):
        return self._cancel_fee

    @cancel_fee.setter
    def cancel_fee(self, value):
        self._cancel_fee = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsOrderInstantdeliveryCancelResponse, self).parse_response_content(response_content)
        if 'cancel_fee' in response:
            self.cancel_fee = response['cancel_fee']
