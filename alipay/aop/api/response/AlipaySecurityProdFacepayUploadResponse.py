#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdFacepayUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdFacepayUploadResponse, self).__init__()
        self._ftoken = None
        self._user_auth_id_hint = None
        self._user_auth_id_type = None

    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value
    @property
    def user_auth_id_hint(self):
        return self._user_auth_id_hint

    @user_auth_id_hint.setter
    def user_auth_id_hint(self, value):
        self._user_auth_id_hint = value
    @property
    def user_auth_id_type(self):
        return self._user_auth_id_type

    @user_auth_id_type.setter
    def user_auth_id_type(self, value):
        self._user_auth_id_type = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdFacepayUploadResponse, self).parse_response_content(response_content)
        if 'ftoken' in response:
            self.ftoken = response['ftoken']
        if 'user_auth_id_hint' in response:
            self.user_auth_id_hint = response['user_auth_id_hint']
        if 'user_auth_id_type' in response:
            self.user_auth_id_type = response['user_auth_id_type']
