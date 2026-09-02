#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasCertCheckResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasCertCheckResponse, self).__init__()
        self._certify_id = None
        self._classify_result = None

    @property
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value
    @property
    def classify_result(self):
        return self._classify_result

    @classify_result.setter
    def classify_result(self, value):
        self._classify_result = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasCertCheckResponse, self).parse_response_content(response_content)
        if 'certify_id' in response:
            self.certify_id = response['certify_id']
        if 'classify_result' in response:
            self.classify_result = response['classify_result']
