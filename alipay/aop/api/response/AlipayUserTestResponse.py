#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserTestResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserTestResponse, self).__init__()
        self._ret1 = None

    @property
    def ret1(self):
        return self._ret1

    @ret1.setter
    def ret1(self, value):
        self._ret1 = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserTestResponse, self).parse_response_content(response_content)
        if 'ret1' in response:
            self.ret1 = response['ret1']
