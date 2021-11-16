#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialOpengreenEnergyCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialOpengreenEnergyCreateResponse, self).__init__()
        self._energy_generated = None
        self._error_code = None
        self._success = None

    @property
    def energy_generated(self):
        return self._energy_generated

    @energy_generated.setter
    def energy_generated(self, value):
        self._energy_generated = value
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
        response = super(AlipaySocialOpengreenEnergyCreateResponse, self).parse_response_content(response_content)
        if 'energy_generated' in response:
            self.energy_generated = response['energy_generated']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'success' in response:
            self.success = response['success']
