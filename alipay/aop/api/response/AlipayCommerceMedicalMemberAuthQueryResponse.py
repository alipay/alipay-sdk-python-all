#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMemberAuthQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMemberAuthQueryResponse, self).__init__()
        self._access_token = None
        self._alipay_id = None
        self._duration = None
        self._expire_time = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMemberAuthQueryResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'alipay_id' in response:
            self.alipay_id = response['alipay_id']
        if 'duration' in response:
            self.duration = response['duration']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
