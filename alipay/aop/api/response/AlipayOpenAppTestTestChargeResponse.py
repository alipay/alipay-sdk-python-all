#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppTestTestChargeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppTestTestChargeResponse, self).__init__()
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppTestTestChargeResponse, self).parse_response_content(response_content)
        if 'name' in response:
            self.name = response['name']
