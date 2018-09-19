#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicMenuGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicMenuGetResponse, self).__init__()
        self._code = None
        self._menu_content = None
        self._msg = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def menu_content(self):
        return self._menu_content

    @menu_content.setter
    def menu_content(self, value):
        self._menu_content = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicMenuGetResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'menu_content' in response:
            self.menu_content = response['menu_content']
        if 'msg' in response:
            self.msg = response['msg']
