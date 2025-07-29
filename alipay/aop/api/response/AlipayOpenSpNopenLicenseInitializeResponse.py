#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNopenLicenseInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNopenLicenseInitializeResponse, self).__init__()
        self._cost_time = None
        self._trace_id_info = None

    @property
    def cost_time(self):
        return self._cost_time

    @cost_time.setter
    def cost_time(self, value):
        self._cost_time = value
    @property
    def trace_id_info(self):
        return self._trace_id_info

    @trace_id_info.setter
    def trace_id_info(self, value):
        self._trace_id_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNopenLicenseInitializeResponse, self).parse_response_content(response_content)
        if 'cost_time' in response:
            self.cost_time = response['cost_time']
        if 'trace_id_info' in response:
            self.trace_id_info = response['trace_id_info']
