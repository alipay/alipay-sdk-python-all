#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsScenePetprofilePlatformprofileCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsScenePetprofilePlatformprofileCheckResponse, self).__init__()
        self._file_url = None
        self._verify_desc = None
        self._verify_result = None

    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def verify_desc(self):
        return self._verify_desc

    @verify_desc.setter
    def verify_desc(self, value):
        self._verify_desc = value
    @property
    def verify_result(self):
        return self._verify_result

    @verify_result.setter
    def verify_result(self, value):
        self._verify_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsScenePetprofilePlatformprofileCheckResponse, self).parse_response_content(response_content)
        if 'file_url' in response:
            self.file_url = response['file_url']
        if 'verify_desc' in response:
            self.verify_desc = response['verify_desc']
        if 'verify_result' in response:
            self.verify_result = response['verify_result']
