#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneYebInfoAdvertisingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneYebInfoAdvertisingQueryResponse, self).__init__()
        self._advertising_type = None

    @property
    def advertising_type(self):
        return self._advertising_type

    @advertising_type.setter
    def advertising_type(self, value):
        self._advertising_type = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneYebInfoAdvertisingQueryResponse, self).parse_response_content(response_content)
        if 'advertising_type' in response:
            self.advertising_type = response['advertising_type']
