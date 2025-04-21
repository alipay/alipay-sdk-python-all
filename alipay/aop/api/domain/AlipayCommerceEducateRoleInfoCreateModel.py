#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateRoleInfoCreateModel(object):

    def __init__(self):
        self._inst_id = None
        self._role_desc = None
        self._role_logo = None
        self._role_name = None
        self._role_type = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def role_desc(self):
        return self._role_desc

    @role_desc.setter
    def role_desc(self, value):
        self._role_desc = value
    @property
    def role_logo(self):
        return self._role_logo

    @role_logo.setter
    def role_logo(self, value):
        self._role_logo = value
    @property
    def role_name(self):
        return self._role_name

    @role_name.setter
    def role_name(self, value):
        self._role_name = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.role_desc:
            if hasattr(self.role_desc, 'to_alipay_dict'):
                params['role_desc'] = self.role_desc.to_alipay_dict()
            else:
                params['role_desc'] = self.role_desc
        if self.role_logo:
            if hasattr(self.role_logo, 'to_alipay_dict'):
                params['role_logo'] = self.role_logo.to_alipay_dict()
            else:
                params['role_logo'] = self.role_logo
        if self.role_name:
            if hasattr(self.role_name, 'to_alipay_dict'):
                params['role_name'] = self.role_name.to_alipay_dict()
            else:
                params['role_name'] = self.role_name
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateRoleInfoCreateModel()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'role_desc' in d:
            o.role_desc = d['role_desc']
        if 'role_logo' in d:
            o.role_logo = d['role_logo']
        if 'role_name' in d:
            o.role_name = d['role_name']
        if 'role_type' in d:
            o.role_type = d['role_type']
        return o


