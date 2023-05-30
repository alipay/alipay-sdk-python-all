#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenAccessTokenDTO(object):

    def __init__(self):
        self._access_token = None
        self._refresh_token = None
        self._refresh_token_expire_time = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value
    @property
    def refresh_token_expire_time(self):
        return self._refresh_token_expire_time

    @refresh_token_expire_time.setter
    def refresh_token_expire_time(self, value):
        self._refresh_token_expire_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.refresh_token:
            if hasattr(self.refresh_token, 'to_alipay_dict'):
                params['refresh_token'] = self.refresh_token.to_alipay_dict()
            else:
                params['refresh_token'] = self.refresh_token
        if self.refresh_token_expire_time:
            if hasattr(self.refresh_token_expire_time, 'to_alipay_dict'):
                params['refresh_token_expire_time'] = self.refresh_token_expire_time.to_alipay_dict()
            else:
                params['refresh_token_expire_time'] = self.refresh_token_expire_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenAccessTokenDTO()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'refresh_token' in d:
            o.refresh_token = d['refresh_token']
        if 'refresh_token_expire_time' in d:
            o.refresh_token_expire_time = d['refresh_token_expire_time']
        return o


