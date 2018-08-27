#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMerchantOperatorRolerelationBindModel(object):

    def __init__(self):
        self._auth_code = None
        self._operator_ids = None
        self._role_id = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def operator_ids(self):
        return self._operator_ids

    @operator_ids.setter
    def operator_ids(self, value):
        if isinstance(value, list):
            self._operator_ids = list()
            for i in value:
                self._operator_ids.append(i)
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
        if self.operator_ids:
            if isinstance(self.operator_ids, list):
                for i in range(0, len(self.operator_ids)):
                    element = self.operator_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operator_ids[i] = element.to_alipay_dict()
            if hasattr(self.operator_ids, 'to_alipay_dict'):
                params['operator_ids'] = self.operator_ids.to_alipay_dict()
            else:
                params['operator_ids'] = self.operator_ids
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
        o = KoubeiMerchantOperatorRolerelationBindModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'operator_ids' in d:
            o.operator_ids = d['operator_ids']
        if 'role_id' in d:
            o.role_id = d['role_id']
        return o


