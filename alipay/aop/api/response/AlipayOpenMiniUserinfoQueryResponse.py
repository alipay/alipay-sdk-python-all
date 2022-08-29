#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniUserinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniUserinfoQueryResponse, self).__init__()
        self._avatar = None
        self._user_id = None
        self._user_name = None

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniUserinfoQueryResponse, self).parse_response_content(response_content)
        if 'avatar' in response:
            self.avatar = response['avatar']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_name' in response:
            self.user_name = response['user_name']
