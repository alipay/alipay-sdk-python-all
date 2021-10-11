#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDeviceBaseinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDeviceBaseinfoQueryResponse, self).__init__()
        self._device_id = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDeviceBaseinfoQueryResponse, self).parse_response_content(response_content)
        if 'device_id' in response:
            self.device_id = response['device_id']
