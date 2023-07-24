#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApmobileApiDetailDTO(object):

    def __init__(self):
        self._api_desc = None
        self._bundle = None
        self._info_name = None
        self._info_type = None
        self._method_info = None
        self._permissions = None
        self._stmt = None

    @property
    def api_desc(self):
        return self._api_desc

    @api_desc.setter
    def api_desc(self, value):
        self._api_desc = value
    @property
    def bundle(self):
        return self._bundle

    @bundle.setter
    def bundle(self, value):
        self._bundle = value
    @property
    def info_name(self):
        return self._info_name

    @info_name.setter
    def info_name(self, value):
        self._info_name = value
    @property
    def info_type(self):
        return self._info_type

    @info_type.setter
    def info_type(self, value):
        self._info_type = value
    @property
    def method_info(self):
        return self._method_info

    @method_info.setter
    def method_info(self, value):
        self._method_info = value
    @property
    def permissions(self):
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        self._permissions = value
    @property
    def stmt(self):
        return self._stmt

    @stmt.setter
    def stmt(self, value):
        self._stmt = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_desc:
            if hasattr(self.api_desc, 'to_alipay_dict'):
                params['api_desc'] = self.api_desc.to_alipay_dict()
            else:
                params['api_desc'] = self.api_desc
        if self.bundle:
            if hasattr(self.bundle, 'to_alipay_dict'):
                params['bundle'] = self.bundle.to_alipay_dict()
            else:
                params['bundle'] = self.bundle
        if self.info_name:
            if hasattr(self.info_name, 'to_alipay_dict'):
                params['info_name'] = self.info_name.to_alipay_dict()
            else:
                params['info_name'] = self.info_name
        if self.info_type:
            if hasattr(self.info_type, 'to_alipay_dict'):
                params['info_type'] = self.info_type.to_alipay_dict()
            else:
                params['info_type'] = self.info_type
        if self.method_info:
            if hasattr(self.method_info, 'to_alipay_dict'):
                params['method_info'] = self.method_info.to_alipay_dict()
            else:
                params['method_info'] = self.method_info
        if self.permissions:
            if hasattr(self.permissions, 'to_alipay_dict'):
                params['permissions'] = self.permissions.to_alipay_dict()
            else:
                params['permissions'] = self.permissions
        if self.stmt:
            if hasattr(self.stmt, 'to_alipay_dict'):
                params['stmt'] = self.stmt.to_alipay_dict()
            else:
                params['stmt'] = self.stmt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileApiDetailDTO()
        if 'api_desc' in d:
            o.api_desc = d['api_desc']
        if 'bundle' in d:
            o.bundle = d['bundle']
        if 'info_name' in d:
            o.info_name = d['info_name']
        if 'info_type' in d:
            o.info_type = d['info_type']
        if 'method_info' in d:
            o.method_info = d['method_info']
        if 'permissions' in d:
            o.permissions = d['permissions']
        if 'stmt' in d:
            o.stmt = d['stmt']
        return o


