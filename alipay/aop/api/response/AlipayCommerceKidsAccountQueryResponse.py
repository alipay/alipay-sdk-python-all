#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceKidsAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceKidsAccountQueryResponse, self).__init__()
        self._login_name = None
        self._user_id = None

    @property
    def login_name(self):
        return self._login_name

    @login_name.setter
    def login_name(self, value):
        self._login_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceKidsAccountQueryResponse, self).parse_response_content(response_content)
        if 'login_name' in response:
            self.login_name = response['login_name']
        if 'user_id' in response:
            self.user_id = response['user_id']
