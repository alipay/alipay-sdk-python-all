#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProdIPRelationVO(object):

    def __init__(self):
        self._ip_alias_name = None
        self._ip_belong_platform = None
        self._ip_code = None
        self._ip_name = None
        self._ip_sub_type = None
        self._ip_type = None
        self._prod_code = None
        self._prod_version = None
        self._role_id = None

    @property
    def ip_alias_name(self):
        return self._ip_alias_name

    @ip_alias_name.setter
    def ip_alias_name(self, value):
        self._ip_alias_name = value
    @property
    def ip_belong_platform(self):
        return self._ip_belong_platform

    @ip_belong_platform.setter
    def ip_belong_platform(self, value):
        self._ip_belong_platform = value
    @property
    def ip_code(self):
        return self._ip_code

    @ip_code.setter
    def ip_code(self, value):
        self._ip_code = value
    @property
    def ip_name(self):
        return self._ip_name

    @ip_name.setter
    def ip_name(self, value):
        self._ip_name = value
    @property
    def ip_sub_type(self):
        return self._ip_sub_type

    @ip_sub_type.setter
    def ip_sub_type(self, value):
        self._ip_sub_type = value
    @property
    def ip_type(self):
        return self._ip_type

    @ip_type.setter
    def ip_type(self, value):
        self._ip_type = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def prod_version(self):
        return self._prod_version

    @prod_version.setter
    def prod_version(self, value):
        self._prod_version = value
    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        self._role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ip_alias_name:
            if hasattr(self.ip_alias_name, 'to_alipay_dict'):
                params['ip_alias_name'] = self.ip_alias_name.to_alipay_dict()
            else:
                params['ip_alias_name'] = self.ip_alias_name
        if self.ip_belong_platform:
            if hasattr(self.ip_belong_platform, 'to_alipay_dict'):
                params['ip_belong_platform'] = self.ip_belong_platform.to_alipay_dict()
            else:
                params['ip_belong_platform'] = self.ip_belong_platform
        if self.ip_code:
            if hasattr(self.ip_code, 'to_alipay_dict'):
                params['ip_code'] = self.ip_code.to_alipay_dict()
            else:
                params['ip_code'] = self.ip_code
        if self.ip_name:
            if hasattr(self.ip_name, 'to_alipay_dict'):
                params['ip_name'] = self.ip_name.to_alipay_dict()
            else:
                params['ip_name'] = self.ip_name
        if self.ip_sub_type:
            if hasattr(self.ip_sub_type, 'to_alipay_dict'):
                params['ip_sub_type'] = self.ip_sub_type.to_alipay_dict()
            else:
                params['ip_sub_type'] = self.ip_sub_type
        if self.ip_type:
            if hasattr(self.ip_type, 'to_alipay_dict'):
                params['ip_type'] = self.ip_type.to_alipay_dict()
            else:
                params['ip_type'] = self.ip_type
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.prod_version:
            if hasattr(self.prod_version, 'to_alipay_dict'):
                params['prod_version'] = self.prod_version.to_alipay_dict()
            else:
                params['prod_version'] = self.prod_version
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
        o = ProdIPRelationVO()
        if 'ip_alias_name' in d:
            o.ip_alias_name = d['ip_alias_name']
        if 'ip_belong_platform' in d:
            o.ip_belong_platform = d['ip_belong_platform']
        if 'ip_code' in d:
            o.ip_code = d['ip_code']
        if 'ip_name' in d:
            o.ip_name = d['ip_name']
        if 'ip_sub_type' in d:
            o.ip_sub_type = d['ip_sub_type']
        if 'ip_type' in d:
            o.ip_type = d['ip_type']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'prod_version' in d:
            o.prod_version = d['prod_version']
        if 'role_id' in d:
            o.role_id = d['role_id']
        return o


