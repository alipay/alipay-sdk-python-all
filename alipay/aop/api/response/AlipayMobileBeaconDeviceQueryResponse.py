#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BeaconDeviceInfo import BeaconDeviceInfo


class AlipayMobileBeaconDeviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobileBeaconDeviceQueryResponse, self).__init__()
        self._beacon_device_info = None
        self._code = None
        self._msg = None

    @property
    def beacon_device_info(self):
        return self._beacon_device_info

    @beacon_device_info.setter
    def beacon_device_info(self, value):
        if isinstance(value, BeaconDeviceInfo):
            self._beacon_device_info = value
        else:
            self._beacon_device_info = BeaconDeviceInfo.from_alipay_dict(value)
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobileBeaconDeviceQueryResponse, self).parse_response_content(response_content)
        if 'beacon_device_info' in response:
            self.beacon_device_info = response['beacon_device_info']
        if 'code' in response:
            self.code = response['code']
        if 'msg' in response:
            self.msg = response['msg']
