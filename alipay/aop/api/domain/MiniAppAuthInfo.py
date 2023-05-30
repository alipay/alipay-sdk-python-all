#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppAuthInfo(object):

    def __init__(self):
        self._auth_app_id = None
        self._auth_time = None
        self._isv_app_id = None
        self._mini_app_token = None

    @property
    def auth_app_id(self):
        return self._auth_app_id

    @auth_app_id.setter
    def auth_app_id(self, value):
        self._auth_app_id = value
    @property
    def auth_time(self):
        return self._auth_time

    @auth_time.setter
    def auth_time(self, value):
        self._auth_time = value
    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value
    @property
    def mini_app_token(self):
        return self._mini_app_token

    @mini_app_token.setter
    def mini_app_token(self, value):
        self._mini_app_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_app_id:
            if hasattr(self.auth_app_id, 'to_alipay_dict'):
                params['auth_app_id'] = self.auth_app_id.to_alipay_dict()
            else:
                params['auth_app_id'] = self.auth_app_id
        if self.auth_time:
            if hasattr(self.auth_time, 'to_alipay_dict'):
                params['auth_time'] = self.auth_time.to_alipay_dict()
            else:
                params['auth_time'] = self.auth_time
        if self.isv_app_id:
            if hasattr(self.isv_app_id, 'to_alipay_dict'):
                params['isv_app_id'] = self.isv_app_id.to_alipay_dict()
            else:
                params['isv_app_id'] = self.isv_app_id
        if self.mini_app_token:
            if hasattr(self.mini_app_token, 'to_alipay_dict'):
                params['mini_app_token'] = self.mini_app_token.to_alipay_dict()
            else:
                params['mini_app_token'] = self.mini_app_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppAuthInfo()
        if 'auth_app_id' in d:
            o.auth_app_id = d['auth_app_id']
        if 'auth_time' in d:
            o.auth_time = d['auth_time']
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        if 'mini_app_token' in d:
            o.mini_app_token = d['mini_app_token']
        return o


