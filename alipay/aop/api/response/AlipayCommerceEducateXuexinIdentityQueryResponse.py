#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateXuexinIdentityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateXuexinIdentityQueryResponse, self).__init__()
        self._college_online_tag = None
        self._graduate_time = None
        self._reason_code = None

    @property
    def college_online_tag(self):
        return self._college_online_tag

    @college_online_tag.setter
    def college_online_tag(self, value):
        self._college_online_tag = value
    @property
    def graduate_time(self):
        return self._graduate_time

    @graduate_time.setter
    def graduate_time(self, value):
        self._graduate_time = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateXuexinIdentityQueryResponse, self).parse_response_content(response_content)
        if 'college_online_tag' in response:
            self.college_online_tag = response['college_online_tag']
        if 'graduate_time' in response:
            self.graduate_time = response['graduate_time']
        if 'reason_code' in response:
            self.reason_code = response['reason_code']
