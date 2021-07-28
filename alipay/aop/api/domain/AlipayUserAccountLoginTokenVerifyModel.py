#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VerifyExtraParams import VerifyExtraParams


class AlipayUserAccountLoginTokenVerifyModel(object):

    def __init__(self):
        self._extra_params = None
        self._login_token = None
        self._source = None

    @property
    def extra_params(self):
        return self._extra_params

    @extra_params.setter
    def extra_params(self, value):
        if isinstance(value, VerifyExtraParams):
            self._extra_params = value
        else:
            self._extra_params = VerifyExtraParams.from_alipay_dict(value)
    @property
    def login_token(self):
        return self._login_token

    @login_token.setter
    def login_token(self, value):
        self._login_token = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.extra_params:
            if hasattr(self.extra_params, 'to_alipay_dict'):
                params['extra_params'] = self.extra_params.to_alipay_dict()
            else:
                params['extra_params'] = self.extra_params
        if self.login_token:
            if hasattr(self.login_token, 'to_alipay_dict'):
                params['login_token'] = self.login_token.to_alipay_dict()
            else:
                params['login_token'] = self.login_token
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAccountLoginTokenVerifyModel()
        if 'extra_params' in d:
            o.extra_params = d['extra_params']
        if 'login_token' in d:
            o.login_token = d['login_token']
        if 'source' in d:
            o.source = d['source']
        return o


