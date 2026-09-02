#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DelegationExtInfo(object):

    def __init__(self):
        self._client_ip = None
        self._user_token = None
        self._user_token_type = None

    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def user_token(self):
        return self._user_token

    @user_token.setter
    def user_token(self, value):
        self._user_token = value
    @property
    def user_token_type(self):
        return self._user_token_type

    @user_token_type.setter
    def user_token_type(self, value):
        self._user_token_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.user_token:
            if hasattr(self.user_token, 'to_alipay_dict'):
                params['user_token'] = self.user_token.to_alipay_dict()
            else:
                params['user_token'] = self.user_token
        if self.user_token_type:
            if hasattr(self.user_token_type, 'to_alipay_dict'):
                params['user_token_type'] = self.user_token_type.to_alipay_dict()
            else:
                params['user_token_type'] = self.user_token_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DelegationExtInfo()
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'user_token' in d:
            o.user_token = d['user_token']
        if 'user_token_type' in d:
            o.user_token_type = d['user_token_type']
        return o


