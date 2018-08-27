#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicQrcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicQrcodeCreateResponse, self).__init__()
        self._code = None
        self._code_img = None
        self._expire_second = None
        self._msg = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def code_img(self):
        return self._code_img

    @code_img.setter
    def code_img(self, value):
        self._code_img = value
    @property
    def expire_second(self):
        return self._expire_second

    @expire_second.setter
    def expire_second(self, value):
        self._expire_second = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicQrcodeCreateResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'code_img' in response:
            self.code_img = response['code_img']
        if 'expire_second' in response:
            self.expire_second = response['expire_second']
        if 'msg' in response:
            self.msg = response['msg']
