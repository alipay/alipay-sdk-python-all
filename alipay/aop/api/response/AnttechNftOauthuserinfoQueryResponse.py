#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftOauthuserinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftOauthuserinfoQueryResponse, self).__init__()
        self._avatar = None
        self._nick_name = None
        self._ou_id = None
        self._phone = None
        self._tu_id = None

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def ou_id(self):
        return self._ou_id

    @ou_id.setter
    def ou_id(self, value):
        self._ou_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def tu_id(self):
        return self._tu_id

    @tu_id.setter
    def tu_id(self, value):
        self._tu_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftOauthuserinfoQueryResponse, self).parse_response_content(response_content)
        if 'avatar' in response:
            self.avatar = response['avatar']
        if 'nick_name' in response:
            self.nick_name = response['nick_name']
        if 'ou_id' in response:
            self.ou_id = response['ou_id']
        if 'phone' in response:
            self.phone = response['phone']
        if 'tu_id' in response:
            self.tu_id = response['tu_id']
