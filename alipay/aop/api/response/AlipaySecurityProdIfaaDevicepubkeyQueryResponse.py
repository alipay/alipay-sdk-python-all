#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdIfaaDevicepubkeyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdIfaaDevicepubkeyQueryResponse, self).__init__()
        self._device_key_info = None

    @property
    def device_key_info(self):
        return self._device_key_info

    @device_key_info.setter
    def device_key_info(self, value):
        self._device_key_info = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdIfaaDevicepubkeyQueryResponse, self).parse_response_content(response_content)
        if 'device_key_info' in response:
            self.device_key_info = response['device_key_info']
