#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderNpassporterVerifyconfigCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNpassporterVerifyconfigCreateResponse, self).__init__()
        self._verify_config_id = None

    @property
    def verify_config_id(self):
        return self._verify_config_id

    @verify_config_id.setter
    def verify_config_id(self, value):
        self._verify_config_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNpassporterVerifyconfigCreateResponse, self).parse_response_content(response_content)
        if 'verify_config_id' in response:
            self.verify_config_id = response['verify_config_id']
