#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceItemGreenenergySendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceItemGreenenergySendResponse, self).__init__()
        self._energy_amount = None
        self._energy_desc = None
        self._log_id = None
        self._result_code = None
        self._result_message = None

    @property
    def energy_amount(self):
        return self._energy_amount

    @energy_amount.setter
    def energy_amount(self, value):
        self._energy_amount = value
    @property
    def energy_desc(self):
        return self._energy_desc

    @energy_desc.setter
    def energy_desc(self, value):
        self._energy_desc = value
    @property
    def log_id(self):
        return self._log_id

    @log_id.setter
    def log_id(self, value):
        self._log_id = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        self._result_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceItemGreenenergySendResponse, self).parse_response_content(response_content)
        if 'energy_amount' in response:
            self.energy_amount = response['energy_amount']
        if 'energy_desc' in response:
            self.energy_desc = response['energy_desc']
        if 'log_id' in response:
            self.log_id = response['log_id']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_message' in response:
            self.result_message = response['result_message']
