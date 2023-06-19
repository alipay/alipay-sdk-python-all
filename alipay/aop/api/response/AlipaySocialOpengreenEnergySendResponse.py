#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialOpengreenEnergySendResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialOpengreenEnergySendResponse, self).__init__()
        self._all_success = None
        self._energy_generate_error_code = None
        self._energy_generate_info = None

    @property
    def all_success(self):
        return self._all_success

    @all_success.setter
    def all_success(self, value):
        self._all_success = value
    @property
    def energy_generate_error_code(self):
        return self._energy_generate_error_code

    @energy_generate_error_code.setter
    def energy_generate_error_code(self, value):
        self._energy_generate_error_code = value
    @property
    def energy_generate_info(self):
        return self._energy_generate_info

    @energy_generate_info.setter
    def energy_generate_info(self, value):
        self._energy_generate_info = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialOpengreenEnergySendResponse, self).parse_response_content(response_content)
        if 'all_success' in response:
            self.all_success = response['all_success']
        if 'energy_generate_error_code' in response:
            self.energy_generate_error_code = response['energy_generate_error_code']
        if 'energy_generate_info' in response:
            self.energy_generate_info = response['energy_generate_info']
