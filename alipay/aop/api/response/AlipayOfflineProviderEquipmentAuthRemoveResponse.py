#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderEquipmentAuthRemoveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderEquipmentAuthRemoveResponse, self).__init__()
        self._device_id = None
        self._merchant_pid = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderEquipmentAuthRemoveResponse, self).parse_response_content(response_content)
        if 'device_id' in response:
            self.device_id = response['device_id']
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
