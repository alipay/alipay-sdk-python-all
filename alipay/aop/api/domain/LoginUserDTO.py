#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LoginUserDTO(object):

    def __init__(self):
        self._ip_role_id = None
        self._tenant_id = None
        self._tenant_name = None

    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def tenant_name(self):
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, value):
        self._tenant_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.tenant_name:
            if hasattr(self.tenant_name, 'to_alipay_dict'):
                params['tenant_name'] = self.tenant_name.to_alipay_dict()
            else:
                params['tenant_name'] = self.tenant_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoginUserDTO()
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'tenant_name' in d:
            o.tenant_name = d['tenant_name']
        return o


