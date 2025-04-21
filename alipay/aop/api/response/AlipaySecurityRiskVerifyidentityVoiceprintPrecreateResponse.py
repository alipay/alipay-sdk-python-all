#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskVerifyidentityVoiceprintPrecreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskVerifyidentityVoiceprintPrecreateResponse, self).__init__()
        self._pre_register_result = None
        self._register_data = None

    @property
    def pre_register_result(self):
        return self._pre_register_result

    @pre_register_result.setter
    def pre_register_result(self, value):
        self._pre_register_result = value
    @property
    def register_data(self):
        return self._register_data

    @register_data.setter
    def register_data(self, value):
        self._register_data = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskVerifyidentityVoiceprintPrecreateResponse, self).parse_response_content(response_content)
        if 'pre_register_result' in response:
            self.pre_register_result = response['pre_register_result']
        if 'register_data' in response:
            self.register_data = response['register_data']
