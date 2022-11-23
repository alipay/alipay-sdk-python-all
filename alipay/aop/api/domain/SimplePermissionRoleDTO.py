#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SimplePermissionRoleDTO(object):

    def __init__(self):
        self._actor_id = None
        self._actor_name = None
        self._permission_role_code = None
        self._permission_role_name = None
        self._permission_role_type = None

    @property
    def actor_id(self):
        return self._actor_id

    @actor_id.setter
    def actor_id(self, value):
        self._actor_id = value
    @property
    def actor_name(self):
        return self._actor_name

    @actor_name.setter
    def actor_name(self, value):
        self._actor_name = value
    @property
    def permission_role_code(self):
        return self._permission_role_code

    @permission_role_code.setter
    def permission_role_code(self, value):
        self._permission_role_code = value
    @property
    def permission_role_name(self):
        return self._permission_role_name

    @permission_role_name.setter
    def permission_role_name(self, value):
        self._permission_role_name = value
    @property
    def permission_role_type(self):
        return self._permission_role_type

    @permission_role_type.setter
    def permission_role_type(self, value):
        self._permission_role_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.actor_id:
            if hasattr(self.actor_id, 'to_alipay_dict'):
                params['actor_id'] = self.actor_id.to_alipay_dict()
            else:
                params['actor_id'] = self.actor_id
        if self.actor_name:
            if hasattr(self.actor_name, 'to_alipay_dict'):
                params['actor_name'] = self.actor_name.to_alipay_dict()
            else:
                params['actor_name'] = self.actor_name
        if self.permission_role_code:
            if hasattr(self.permission_role_code, 'to_alipay_dict'):
                params['permission_role_code'] = self.permission_role_code.to_alipay_dict()
            else:
                params['permission_role_code'] = self.permission_role_code
        if self.permission_role_name:
            if hasattr(self.permission_role_name, 'to_alipay_dict'):
                params['permission_role_name'] = self.permission_role_name.to_alipay_dict()
            else:
                params['permission_role_name'] = self.permission_role_name
        if self.permission_role_type:
            if hasattr(self.permission_role_type, 'to_alipay_dict'):
                params['permission_role_type'] = self.permission_role_type.to_alipay_dict()
            else:
                params['permission_role_type'] = self.permission_role_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SimplePermissionRoleDTO()
        if 'actor_id' in d:
            o.actor_id = d['actor_id']
        if 'actor_name' in d:
            o.actor_name = d['actor_name']
        if 'permission_role_code' in d:
            o.permission_role_code = d['permission_role_code']
        if 'permission_role_name' in d:
            o.permission_role_name = d['permission_role_name']
        if 'permission_role_type' in d:
            o.permission_role_type = d['permission_role_type']
        return o


