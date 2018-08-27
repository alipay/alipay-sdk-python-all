#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPlatformUseridGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPlatformUseridGetResponse, self).__init__()
        self._dict = None

    @property
    def dict(self):
        return self._dict

    @dict.setter
    def dict(self, value):
        self._dict = value

    def parse_response_content(self, response_content):
        response = super(AlipayPlatformUseridGetResponse, self).parse_response_content(response_content)
        if 'dict' in response:
            self.dict = response['dict']
