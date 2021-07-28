#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditUserInfoShareQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditUserInfoShareQueryResponse, self).__init__()
        self._avatar = None
        self._city = None
        self._gender = None
        self._nick_name = None
        self._province = None
        self._user_id = None

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditUserInfoShareQueryResponse, self).parse_response_content(response_content)
        if 'avatar' in response:
            self.avatar = response['avatar']
        if 'city' in response:
            self.city = response['city']
        if 'gender' in response:
            self.gender = response['gender']
        if 'nick_name' in response:
            self.nick_name = response['nick_name']
        if 'province' in response:
            self.province = response['province']
        if 'user_id' in response:
            self.user_id = response['user_id']
