#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsScenePetprofilePlatformprofileIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsScenePetprofilePlatformprofileIdentifyResponse, self).__init__()
        self._verify_result = None

    @property
    def verify_result(self):
        return self._verify_result

    @verify_result.setter
    def verify_result(self, value):
        self._verify_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsScenePetprofilePlatformprofileIdentifyResponse, self).parse_response_content(response_content)
        if 'verify_result' in response:
            self.verify_result = response['verify_result']
