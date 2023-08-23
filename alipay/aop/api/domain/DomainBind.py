#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DomainBind(object):

    def __init__(self):
        self._bind_id = None
        self._domain_name = None
        self._function_name = None
        self._gmt_create = None
        self._gmt_modified = None
        self._is_custom = None
        self._need_sign = None
        self._path = None

    @property
    def bind_id(self):
        return self._bind_id

    @bind_id.setter
    def bind_id(self, value):
        self._bind_id = value
    @property
    def domain_name(self):
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        self._domain_name = value
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def is_custom(self):
        return self._is_custom

    @is_custom.setter
    def is_custom(self, value):
        self._is_custom = value
    @property
    def need_sign(self):
        return self._need_sign

    @need_sign.setter
    def need_sign(self, value):
        self._need_sign = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_id:
            if hasattr(self.bind_id, 'to_alipay_dict'):
                params['bind_id'] = self.bind_id.to_alipay_dict()
            else:
                params['bind_id'] = self.bind_id
        if self.domain_name:
            if hasattr(self.domain_name, 'to_alipay_dict'):
                params['domain_name'] = self.domain_name.to_alipay_dict()
            else:
                params['domain_name'] = self.domain_name
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.is_custom:
            if hasattr(self.is_custom, 'to_alipay_dict'):
                params['is_custom'] = self.is_custom.to_alipay_dict()
            else:
                params['is_custom'] = self.is_custom
        if self.need_sign:
            if hasattr(self.need_sign, 'to_alipay_dict'):
                params['need_sign'] = self.need_sign.to_alipay_dict()
            else:
                params['need_sign'] = self.need_sign
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DomainBind()
        if 'bind_id' in d:
            o.bind_id = d['bind_id']
        if 'domain_name' in d:
            o.domain_name = d['domain_name']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'is_custom' in d:
            o.is_custom = d['is_custom']
        if 'need_sign' in d:
            o.need_sign = d['need_sign']
        if 'path' in d:
            o.path = d['path']
        return o


