#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiFqqrcodeHbfqBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiFqqrcodeHbfqBindResponse, self).__init__()
        self._bind = None

    @property
    def bind(self):
        return self._bind

    @bind.setter
    def bind(self, value):
        self._bind = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiFqqrcodeHbfqBindResponse, self).parse_response_content(response_content)
        if 'bind' in response:
            self.bind = response['bind']
