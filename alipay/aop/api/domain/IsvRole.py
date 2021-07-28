#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvRole(object):

    def __init__(self):
        self._role_id = None
        self._role_name = None

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
        o = IsvRole()
        if 'role_id' in d:
            o.role_id = d['role_id']
        if 'role_name' in d:
            o.role_name = d['role_name']
        return o


