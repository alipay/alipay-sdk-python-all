#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskAudioVerifyResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskAudioVerifyResponse, self).__init__()
        self._request_id = None
        self._unique_id = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskAudioVerifyResponse, self).parse_response_content(response_content)
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
