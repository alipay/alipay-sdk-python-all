#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskDirectionalRainscoreQueryModel(object):

    def __init__(self):
        self._account = None
        self._account_type = None
        self._version = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.version:
            if hasattr(self.version, 'to_alipay_dict'):
                params['version'] = self.version.to_alipay_dict()
            else:
                params['version'] = self.version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskDirectionalRainscoreQueryModel()
        if 'account' in d:
            o.account = d['account']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'version' in d:
            o.version = d['version']
        return o


