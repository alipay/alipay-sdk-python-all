#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIsponetestComputertestQuickcreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIsponetestComputertestQuickcreateResponse, self).__init__()
        self._dddd = None

    @property
    def dddd(self):
        return self._dddd

    @dddd.setter
    def dddd(self, value):
        self._dddd = value

    def parse_response_content(self, response_content):
        response = super(AlipayIsponetestComputertestQuickcreateResponse, self).parse_response_content(response_content)
        if 'dddd' in response:
            self.dddd = response['dddd']
