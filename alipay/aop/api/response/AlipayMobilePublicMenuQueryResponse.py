#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicMenuQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicMenuQueryResponse, self).__init__()
        self._all_menu_list = None
        self._code = None
        self._msg = None

    @property
    def all_menu_list(self):
        return self._all_menu_list

    @all_menu_list.setter
    def all_menu_list(self, value):
        self._all_menu_list = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicMenuQueryResponse, self).parse_response_content(response_content)
        if 'all_menu_list' in response:
            self.all_menu_list = response['all_menu_list']
        if 'code' in response:
            self.code = response['code']
        if 'msg' in response:
            self.msg = response['msg']
