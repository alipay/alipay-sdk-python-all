#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZmAuthParams import ZmAuthParams
from alipay.aop.api.domain.ExtendParams import ExtendParams


class AlipayOpenMytestoQueryModel(object):

    def __init__(self):
        self._auth = None
        self._extend_params = None

    @property
    def auth(self):
        return self._auth

    @auth.setter
    def auth(self, value):
        if isinstance(value, ZmAuthParams):
            self._auth = value
        else:
            self._auth = ZmAuthParams.from_alipay_dict(value)
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, ExtendParams):
            self._extend_params = value
        else:
            self._extend_params = ExtendParams.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.auth:
            if hasattr(self.auth, 'to_alipay_dict'):
                params['auth'] = self.auth.to_alipay_dict()
            else:
                params['auth'] = self.auth
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMytestoQueryModel()
        if 'auth' in d:
            o.auth = d['auth']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        return o


