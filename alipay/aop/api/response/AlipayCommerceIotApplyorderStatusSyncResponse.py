#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotApplyorderStatusSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotApplyorderStatusSyncResponse, self).__init__()
        self._device_amount = None

    @property
    def device_amount(self):
        return self._device_amount

    @device_amount.setter
    def device_amount(self, value):
        self._device_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotApplyorderStatusSyncResponse, self).parse_response_content(response_content)
        if 'device_amount' in response:
            self.device_amount = response['device_amount']
