#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAccountTaobaoBindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountTaobaoBindQueryResponse, self).__init__()
        self._avatar = None
        self._email = None
        self._is_certified = None
        self._mobile_no = None
        self._nick_name = None
        self._open_id = None
        self._user_id = None
        self._user_type = None

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def is_certified(self):
        return self._is_certified

    @is_certified.setter
    def is_certified(self, value):
        self._is_certified = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountTaobaoBindQueryResponse, self).parse_response_content(response_content)
        if 'avatar' in response:
            self.avatar = response['avatar']
        if 'email' in response:
            self.email = response['email']
        if 'is_certified' in response:
            self.is_certified = response['is_certified']
        if 'mobile_no' in response:
            self.mobile_no = response['mobile_no']
        if 'nick_name' in response:
            self.nick_name = response['nick_name']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_type' in response:
            self.user_type = response['user_type']
