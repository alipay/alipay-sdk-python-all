#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMerchantOperatorRoleDeleteModel(object):

    def __init__(self):
        self._auth_code = None
        self._role_id = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        self._role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.role_id:
            if hasattr(self.role_id, 'to_alipay_dict'):
                params['role_id'] = self.role_id.to_alipay_dict()
            else:
                params['role_id'] = self.role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMerchantOperatorRoleDeleteModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'role_id' in d:
            o.role_id = d['role_id']
        return o


