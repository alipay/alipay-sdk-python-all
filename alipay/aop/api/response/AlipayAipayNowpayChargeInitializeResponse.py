#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayNowpayChargeInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayNowpayChargeInitializeResponse, self).__init__()
        self._configuration_qr_code = None
        self._configuration_url = None
        self._management_url = None

    @property
    def configuration_qr_code(self):
        return self._configuration_qr_code

    @configuration_qr_code.setter
    def configuration_qr_code(self, value):
        self._configuration_qr_code = value
    @property
    def configuration_url(self):
        return self._configuration_url

    @configuration_url.setter
    def configuration_url(self, value):
        self._configuration_url = value
    @property
    def management_url(self):
        return self._management_url

    @management_url.setter
    def management_url(self, value):
        self._management_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayNowpayChargeInitializeResponse, self).parse_response_content(response_content)
        if 'configuration_qr_code' in response:
            self.configuration_qr_code = response['configuration_qr_code']
        if 'configuration_url' in response:
            self.configuration_url = response['configuration_url']
        if 'management_url' in response:
            self.management_url = response['management_url']
