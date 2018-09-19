#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPlatformOpenidGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPlatformOpenidGetResponse, self).__init__()
        self._code = None
        self._dict = None
        self._msg = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def dict(self):
        return self._dict

    @dict.setter
    def dict(self, value):
        self._dict = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayPlatformOpenidGetResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'dict' in response:
            self.dict = response['dict']
        if 'msg' in response:
            self.msg = response['msg']
