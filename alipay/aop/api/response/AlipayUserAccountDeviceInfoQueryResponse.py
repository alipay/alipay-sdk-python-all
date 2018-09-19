#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceResultInfo import DeviceResultInfo


class AlipayUserAccountDeviceInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountDeviceInfoQueryResponse, self).__init__()
        self._device_infos = None
        self._device_type = None
        self._encrypt_type = None
        self._result_code = None

    @property
    def device_infos(self):
        return self._device_infos

    @device_infos.setter
    def device_infos(self, value):
        if isinstance(value, list):
            self._device_infos = list()
            for i in value:
                if isinstance(i, DeviceResultInfo):
                    self._device_infos.append(i)
                else:
                    self._device_infos.append(DeviceResultInfo.from_alipay_dict(i))
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def encrypt_type(self):
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, value):
        self._encrypt_type = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountDeviceInfoQueryResponse, self).parse_response_content(response_content)
        if 'device_infos' in response:
            self.device_infos = response['device_infos']
        if 'device_type' in response:
            self.device_type = response['device_type']
        if 'encrypt_type' in response:
            self.encrypt_type = response['encrypt_type']
        if 'result_code' in response:
            self.result_code = response['result_code']
