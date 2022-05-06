#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialOpengreenEnergyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialOpengreenEnergyQueryResponse, self).__init__()
        self._energy_info = None
        self._error_code = None
        self._success = None

    @property
    def energy_info(self):
        return self._energy_info

    @energy_info.setter
    def energy_info(self, value):
        self._energy_info = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialOpengreenEnergyQueryResponse, self).parse_response_content(response_content)
        if 'energy_info' in response:
            self.energy_info = response['energy_info']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'success' in response:
            self.success = response['success']
