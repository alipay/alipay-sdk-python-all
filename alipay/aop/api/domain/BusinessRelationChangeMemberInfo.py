#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessRelationChangeMemberInfo(object):

    def __init__(self):
        self._change_code = None
        self._ip_role_desc = None
        self._ip_role_id = None
        self._ip_role_type = None

    @property
    def change_code(self):
        return self._change_code

    @change_code.setter
    def change_code(self, value):
        self._change_code = value
    @property
    def ip_role_desc(self):
        return self._ip_role_desc

    @ip_role_desc.setter
    def ip_role_desc(self, value):
        self._ip_role_desc = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def ip_role_type(self):
        return self._ip_role_type

    @ip_role_type.setter
    def ip_role_type(self, value):
        self._ip_role_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_code:
            if hasattr(self.change_code, 'to_alipay_dict'):
                params['change_code'] = self.change_code.to_alipay_dict()
            else:
                params['change_code'] = self.change_code
        if self.ip_role_desc:
            if hasattr(self.ip_role_desc, 'to_alipay_dict'):
                params['ip_role_desc'] = self.ip_role_desc.to_alipay_dict()
            else:
                params['ip_role_desc'] = self.ip_role_desc
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.ip_role_type:
            if hasattr(self.ip_role_type, 'to_alipay_dict'):
                params['ip_role_type'] = self.ip_role_type.to_alipay_dict()
            else:
                params['ip_role_type'] = self.ip_role_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessRelationChangeMemberInfo()
        if 'change_code' in d:
            o.change_code = d['change_code']
        if 'ip_role_desc' in d:
            o.ip_role_desc = d['ip_role_desc']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'ip_role_type' in d:
            o.ip_role_type = d['ip_role_type']
        return o


