#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EapAuthVO(object):

    def __init__(self):
        self._corp = None
        self._has_auth = None

    @property
    def corp(self):
        return self._corp

    @corp.setter
    def corp(self, value):
        self._corp = value
    @property
    def has_auth(self):
        return self._has_auth

    @has_auth.setter
    def has_auth(self, value):
        self._has_auth = value


    def to_alipay_dict(self):
        params = dict()
        if self.corp:
            if hasattr(self.corp, 'to_alipay_dict'):
                params['corp'] = self.corp.to_alipay_dict()
            else:
                params['corp'] = self.corp
        if self.has_auth:
            if hasattr(self.has_auth, 'to_alipay_dict'):
                params['has_auth'] = self.has_auth.to_alipay_dict()
            else:
                params['has_auth'] = self.has_auth
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EapAuthVO()
        if 'corp' in d:
            o.corp = d['corp']
        if 'has_auth' in d:
            o.has_auth = d['has_auth']
        return o


