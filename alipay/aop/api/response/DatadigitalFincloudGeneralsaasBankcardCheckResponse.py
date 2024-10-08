#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasBankcardCheckResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasBankcardCheckResponse, self).__init__()
        self._certify_id = None
        self._detail = None
        self._match = None

    @property
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value
    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, value):
        self._match = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasBankcardCheckResponse, self).parse_response_content(response_content)
        if 'certify_id' in response:
            self.certify_id = response['certify_id']
        if 'detail' in response:
            self.detail = response['detail']
        if 'match' in response:
            self.match = response['match']
