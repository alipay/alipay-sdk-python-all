#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthResult(object):

    def __init__(self):
        self._access_token = None
        self._expires_in = None
        self._open_id = None
        self._re_expires_in = None
        self._user_id = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def expires_in(self):
        return self._expires_in

    @expires_in.setter
    def expires_in(self, value):
        self._expires_in = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def re_expires_in(self):
        return self._re_expires_in

    @re_expires_in.setter
    def re_expires_in(self, value):
        self._re_expires_in = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.expires_in:
            if hasattr(self.expires_in, 'to_alipay_dict'):
                params['expires_in'] = self.expires_in.to_alipay_dict()
            else:
                params['expires_in'] = self.expires_in
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.re_expires_in:
            if hasattr(self.re_expires_in, 'to_alipay_dict'):
                params['re_expires_in'] = self.re_expires_in.to_alipay_dict()
            else:
                params['re_expires_in'] = self.re_expires_in
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthResult()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'expires_in' in d:
            o.expires_in = d['expires_in']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 're_expires_in' in d:
            o.re_expires_in = d['re_expires_in']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


