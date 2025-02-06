#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CancelCommissionRoleInfo(object):

    def __init__(self):
        self._role_alipay_account = None
        self._role_level = None

    @property
    def role_alipay_account(self):
        return self._role_alipay_account

    @role_alipay_account.setter
    def role_alipay_account(self, value):
        self._role_alipay_account = value
    @property
    def role_level(self):
        return self._role_level

    @role_level.setter
    def role_level(self, value):
        self._role_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.role_alipay_account:
            if hasattr(self.role_alipay_account, 'to_alipay_dict'):
                params['role_alipay_account'] = self.role_alipay_account.to_alipay_dict()
            else:
                params['role_alipay_account'] = self.role_alipay_account
        if self.role_level:
            if hasattr(self.role_level, 'to_alipay_dict'):
                params['role_level'] = self.role_level.to_alipay_dict()
            else:
                params['role_level'] = self.role_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CancelCommissionRoleInfo()
        if 'role_alipay_account' in d:
            o.role_alipay_account = d['role_alipay_account']
        if 'role_level' in d:
            o.role_level = d['role_level']
        return o


