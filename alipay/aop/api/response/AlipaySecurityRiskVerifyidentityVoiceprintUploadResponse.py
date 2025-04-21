#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskVerifyidentityVoiceprintUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskVerifyidentityVoiceprintUploadResponse, self).__init__()
        self._device_data = None

    @property
    def device_data(self):
        return self._device_data

    @device_data.setter
    def device_data(self, value):
        self._device_data = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskVerifyidentityVoiceprintUploadResponse, self).parse_response_content(response_content)
        if 'device_data' in response:
            self.device_data = response['device_data']
