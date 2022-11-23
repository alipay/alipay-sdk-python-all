#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppTestGrayCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppTestGrayCreateResponse, self).__init__()
        self._zone_name = None

    @property
    def zone_name(self):
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value):
        self._zone_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppTestGrayCreateResponse, self).parse_response_content(response_content)
        if 'zone_name' in response:
            self.zone_name = response['zone_name']
