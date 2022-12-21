#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDeviceEcobindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDeviceEcobindQueryResponse, self).__init__()
        self._bind = None
        self._bind_type = None
        self._user_id = None

    @property
    def bind(self):
        return self._bind

    @bind.setter
    def bind(self, value):
        self._bind = value
    @property
    def bind_type(self):
        return self._bind_type

    @bind_type.setter
    def bind_type(self, value):
        self._bind_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDeviceEcobindQueryResponse, self).parse_response_content(response_content)
        if 'bind' in response:
            self.bind = response['bind']
        if 'bind_type' in response:
            self.bind_type = response['bind_type']
        if 'user_id' in response:
            self.user_id = response['user_id']
