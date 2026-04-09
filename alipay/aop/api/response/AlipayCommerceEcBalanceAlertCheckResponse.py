#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcBalanceAlertCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcBalanceAlertCheckResponse, self).__init__()
        self._sufficient = None

    @property
    def sufficient(self):
        return self._sufficient

    @sufficient.setter
    def sufficient(self, value):
        self._sufficient = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcBalanceAlertCheckResponse, self).parse_response_content(response_content)
        if 'sufficient' in response:
            self.sufficient = response['sufficient']
