#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditFinancePayAccountInfo(object):

    def __init__(self):
        self._account_ext = None
        self._identity = None
        self._identity_type = None

    @property
    def account_ext(self):
        return self._account_ext

    @account_ext.setter
    def account_ext(self, value):
        self._account_ext = value
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_ext:
            if hasattr(self.account_ext, 'to_alipay_dict'):
                params['account_ext'] = self.account_ext.to_alipay_dict()
            else:
                params['account_ext'] = self.account_ext
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditFinancePayAccountInfo()
        if 'account_ext' in d:
            o.account_ext = d['account_ext']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        return o


