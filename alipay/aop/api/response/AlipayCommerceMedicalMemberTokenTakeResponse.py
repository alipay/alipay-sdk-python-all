#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMemberTokenTakeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMemberTokenTakeResponse, self).__init__()
        self._access_token = None
        self._expire_time = None
        self._source = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMemberTokenTakeResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'source' in response:
            self.source = response['source']
