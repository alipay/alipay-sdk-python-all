#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAlideviceinfoOfflinecodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAlideviceinfoOfflinecodeCreateResponse, self).__init__()
        self._biz_tid = None
        self._token = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAlideviceinfoOfflinecodeCreateResponse, self).parse_response_content(response_content)
        if 'biz_tid' in response:
            self.biz_tid = response['biz_tid']
        if 'token' in response:
            self.token = response['token']
