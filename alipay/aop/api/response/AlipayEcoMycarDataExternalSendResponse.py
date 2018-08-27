#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarDataExternalSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarDataExternalSendResponse, self).__init__()
        self._external_system_name = None
        self._process_result = None

    @property
    def external_system_name(self):
        return self._external_system_name

    @external_system_name.setter
    def external_system_name(self, value):
        self._external_system_name = value
    @property
    def process_result(self):
        return self._process_result

    @process_result.setter
    def process_result(self, value):
        self._process_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarDataExternalSendResponse, self).parse_response_content(response_content)
        if 'external_system_name' in response:
            self.external_system_name = response['external_system_name']
        if 'process_result' in response:
            self.process_result = response['process_result']
