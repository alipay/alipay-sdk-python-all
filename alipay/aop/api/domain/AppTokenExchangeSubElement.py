#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppTokenExchangeSubElement(object):

    def __init__(self):
        self._app_auth_token = None
        self._app_refresh_token = None
        self._auth_app_id = None
        self._expires_in = None
        self._re_expires_in = None
        self._user_id = None

    @property
    def app_auth_token(self):
        return self._app_auth_token

    @app_auth_token.setter
    def app_auth_token(self, value):
        self._app_auth_token = value
    @property
    def app_refresh_token(self):
        return self._app_refresh_token

    @app_refresh_token.setter
    def app_refresh_token(self, value):
        self._app_refresh_token = value
    @property
    def auth_app_id(self):
        return self._auth_app_id

    @auth_app_id.setter
    def auth_app_id(self, value):
        self._auth_app_id = value
    @property
    def expires_in(self):
        return self._expires_in

    @expires_in.setter
    def expires_in(self, value):
        self._expires_in = value
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
        if self.app_auth_token:
            if hasattr(self.app_auth_token, 'to_alipay_dict'):
                params['app_auth_token'] = self.app_auth_token.to_alipay_dict()
            else:
                params['app_auth_token'] = self.app_auth_token
        if self.app_refresh_token:
            if hasattr(self.app_refresh_token, 'to_alipay_dict'):
                params['app_refresh_token'] = self.app_refresh_token.to_alipay_dict()
            else:
                params['app_refresh_token'] = self.app_refresh_token
        if self.auth_app_id:
            if hasattr(self.auth_app_id, 'to_alipay_dict'):
                params['auth_app_id'] = self.auth_app_id.to_alipay_dict()
            else:
                params['auth_app_id'] = self.auth_app_id
        if self.expires_in:
            if hasattr(self.expires_in, 'to_alipay_dict'):
                params['expires_in'] = self.expires_in.to_alipay_dict()
            else:
                params['expires_in'] = self.expires_in
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
        o = AppTokenExchangeSubElement()
        if 'app_auth_token' in d:
            o.app_auth_token = d['app_auth_token']
        if 'app_refresh_token' in d:
            o.app_refresh_token = d['app_refresh_token']
        if 'auth_app_id' in d:
            o.auth_app_id = d['auth_app_id']
        if 'expires_in' in d:
            o.expires_in = d['expires_in']
        if 're_expires_in' in d:
            o.re_expires_in = d['re_expires_in']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


