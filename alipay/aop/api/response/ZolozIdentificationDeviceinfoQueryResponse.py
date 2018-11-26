#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZolozDeviceInfo import ZolozDeviceInfo


class ZolozIdentificationDeviceinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZolozIdentificationDeviceinfoQueryResponse, self).__init__()
        self._device_info = None

    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        if isinstance(value, ZolozDeviceInfo):
            self._device_info = value
        else:
            self._device_info = ZolozDeviceInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZolozIdentificationDeviceinfoQueryResponse, self).parse_response_content(response_content)
        if 'device_info' in response:
            self.device_info = response['device_info']
