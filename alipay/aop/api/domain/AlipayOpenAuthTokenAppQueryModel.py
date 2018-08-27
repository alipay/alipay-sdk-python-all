#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAuthTokenAppQueryModel(object):

    def __init__(self):
        self._app_auth_token = None

    @property
    def app_auth_token(self):
        return self._app_auth_token

    @app_auth_token.setter
    def app_auth_token(self, value):
        self._app_auth_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_auth_token:
            if hasattr(self.app_auth_token, 'to_alipay_dict'):
                params['app_auth_token'] = self.app_auth_token.to_alipay_dict()
            else:
                params['app_auth_token'] = self.app_auth_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthTokenAppQueryModel()
        if 'app_auth_token' in d:
            o.app_auth_token = d['app_auth_token']
        return o


