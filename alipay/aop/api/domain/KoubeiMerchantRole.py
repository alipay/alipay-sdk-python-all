#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMerchantRole(object):

    def __init__(self):
        self._operator_num = None
        self._permission_num = None
        self._role_code = None
        self._role_id = None
        self._role_name = None

    @property
    def operator_num(self):
        return self._operator_num

    @operator_num.setter
    def operator_num(self, value):
        self._operator_num = value
    @property
    def permission_num(self):
        return self._permission_num

    @permission_num.setter
    def permission_num(self, value):
        self._permission_num = value
    @property
    def role_code(self):
        return self._role_code

    @role_code.setter
    def role_code(self, value):
        self._role_code = value
    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        self._role_id = value
    @property
    def role_name(self):
        return self._role_name

    @role_name.setter
    def role_name(self, value):
        self._role_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator_num:
            if hasattr(self.operator_num, 'to_alipay_dict'):
                params['operator_num'] = self.operator_num.to_alipay_dict()
            else:
                params['operator_num'] = self.operator_num
        if self.permission_num:
            if hasattr(self.permission_num, 'to_alipay_dict'):
                params['permission_num'] = self.permission_num.to_alipay_dict()
            else:
                params['permission_num'] = self.permission_num
        if self.role_code:
            if hasattr(self.role_code, 'to_alipay_dict'):
                params['role_code'] = self.role_code.to_alipay_dict()
            else:
                params['role_code'] = self.role_code
        if self.role_id:
            if hasattr(self.role_id, 'to_alipay_dict'):
                params['role_id'] = self.role_id.to_alipay_dict()
            else:
                params['role_id'] = self.role_id
        if self.role_name:
            if hasattr(self.role_name, 'to_alipay_dict'):
                params['role_name'] = self.role_name.to_alipay_dict()
            else:
                params['role_name'] = self.role_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMerchantRole()
        if 'operator_num' in d:
            o.operator_num = d['operator_num']
        if 'permission_num' in d:
            o.permission_num = d['permission_num']
        if 'role_code' in d:
            o.role_code = d['role_code']
        if 'role_id' in d:
            o.role_id = d['role_id']
        if 'role_name' in d:
            o.role_name = d['role_name']
        return o


