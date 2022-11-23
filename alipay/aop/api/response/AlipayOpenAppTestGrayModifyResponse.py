#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppTestGrayModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppTestGrayModifyResponse, self).__init__()
        self._address = None
        self._zone_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def zone_name(self):
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value):
        self._zone_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppTestGrayModifyResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'zone_name' in response:
            self.zone_name = response['zone_name']
