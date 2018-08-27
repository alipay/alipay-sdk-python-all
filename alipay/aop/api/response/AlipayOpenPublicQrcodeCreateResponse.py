#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicQrcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicQrcodeCreateResponse, self).__init__()
        self._code_img = None
        self._expire_second = None

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

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicQrcodeCreateResponse, self).parse_response_content(response_content)
        if 'code_img' in response:
            self.code_img = response['code_img']
        if 'expire_second' in response:
            self.expire_second = response['expire_second']
