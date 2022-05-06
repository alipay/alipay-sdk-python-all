#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceGreenItemenergySendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceGreenItemenergySendResponse, self).__init__()
        self._energy_amount = None

    @property
    def energy_amount(self):
        return self._energy_amount

    @energy_amount.setter
    def energy_amount(self, value):
        self._energy_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceGreenItemenergySendResponse, self).parse_response_content(response_content)
        if 'energy_amount' in response:
            self.energy_amount = response['energy_amount']
