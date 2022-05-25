#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAccountInfoTaobaoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountInfoTaobaoQueryResponse, self).__init__()
        self._alipay_user_id = None
        self._is_certified = None
        self._login_id = None
        self._user_type = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def is_certified(self):
        return self._is_certified

    @is_certified.setter
    def is_certified(self, value):
        self._is_certified = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountInfoTaobaoQueryResponse, self).parse_response_content(response_content)
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'is_certified' in response:
            self.is_certified = response['is_certified']
        if 'login_id' in response:
            self.login_id = response['login_id']
        if 'user_type' in response:
            self.user_type = response['user_type']
