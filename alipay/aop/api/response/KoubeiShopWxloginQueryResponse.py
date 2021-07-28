#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiShopWxloginQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiShopWxloginQueryResponse, self).__init__()
        self._openid = None
        self._session_key = None

    @property
    def openid(self):
        return self._openid

    @openid.setter
    def openid(self, value):
        self._openid = value
    @property
    def session_key(self):
        return self._session_key

    @session_key.setter
    def session_key(self, value):
        self._session_key = value

    def parse_response_content(self, response_content):
        response = super(KoubeiShopWxloginQueryResponse, self).parse_response_content(response_content)
        if 'openid' in response:
            self.openid = response['openid']
        if 'session_key' in response:
            self.session_key = response['session_key']
