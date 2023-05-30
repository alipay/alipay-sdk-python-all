#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiRoleInfo(object):

    def __init__(self):
        self._role_type = None
        self._sub_role_type = None

    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def sub_role_type(self):
        return self._sub_role_type

    @sub_role_type.setter
    def sub_role_type(self, value):
        self._sub_role_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        if self.sub_role_type:
            if hasattr(self.sub_role_type, 'to_alipay_dict'):
                params['sub_role_type'] = self.sub_role_type.to_alipay_dict()
            else:
                params['sub_role_type'] = self.sub_role_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiRoleInfo()
        if 'role_type' in d:
            o.role_type = d['role_type']
        if 'sub_role_type' in d:
            o.sub_role_type = d['sub_role_type']
        return o


