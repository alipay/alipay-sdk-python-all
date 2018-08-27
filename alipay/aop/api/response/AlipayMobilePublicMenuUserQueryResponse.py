#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicMenuUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicMenuUserQueryResponse, self).__init__()
        self._code = None
        self._menu_key = None
        self._msg = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def menu_key(self):
        return self._menu_key

    @menu_key.setter
    def menu_key(self, value):
        self._menu_key = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicMenuUserQueryResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'menu_key' in response:
            self.menu_key = response['menu_key']
        if 'msg' in response:
            self.msg = response['msg']
