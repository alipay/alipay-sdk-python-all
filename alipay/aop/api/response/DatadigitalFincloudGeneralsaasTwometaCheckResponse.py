#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasTwometaCheckResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasTwometaCheckResponse, self).__init__()
        self._certify_id = None
        self._match = None

    @property
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value
    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, value):
        self._match = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasTwometaCheckResponse, self).parse_response_content(response_content)
        if 'certify_id' in response:
            self.certify_id = response['certify_id']
        if 'match' in response:
            self.match = response['match']
