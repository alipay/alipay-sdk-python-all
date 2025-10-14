#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAccountBaseInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountBaseInfoQueryResponse, self).__init__()
        self._bind_mobile = None
        self._bind_mobile_time = None
        self._phone_release_sign = None

    @property
    def bind_mobile(self):
        return self._bind_mobile

    @bind_mobile.setter
    def bind_mobile(self, value):
        self._bind_mobile = value
    @property
    def bind_mobile_time(self):
        return self._bind_mobile_time

    @bind_mobile_time.setter
    def bind_mobile_time(self, value):
        self._bind_mobile_time = value
    @property
    def phone_release_sign(self):
        return self._phone_release_sign

    @phone_release_sign.setter
    def phone_release_sign(self, value):
        self._phone_release_sign = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountBaseInfoQueryResponse, self).parse_response_content(response_content)
        if 'bind_mobile' in response:
            self.bind_mobile = response['bind_mobile']
        if 'bind_mobile_time' in response:
            self.bind_mobile_time = response['bind_mobile_time']
        if 'phone_release_sign' in response:
            self.phone_release_sign = response['phone_release_sign']
