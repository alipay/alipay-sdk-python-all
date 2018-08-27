#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessPermission(object):

    def __init__(self):
        self._domain = None
        self._permission_code = None
        self._source_permission_code = None

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value
    @property
    def permission_code(self):
        return self._permission_code

    @permission_code.setter
    def permission_code(self, value):
        self._permission_code = value
    @property
    def source_permission_code(self):
        return self._source_permission_code

    @source_permission_code.setter
    def source_permission_code(self, value):
        self._source_permission_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.domain:
            if hasattr(self.domain, 'to_alipay_dict'):
                params['domain'] = self.domain.to_alipay_dict()
            else:
                params['domain'] = self.domain
        if self.permission_code:
            if hasattr(self.permission_code, 'to_alipay_dict'):
                params['permission_code'] = self.permission_code.to_alipay_dict()
            else:
                params['permission_code'] = self.permission_code
        if self.source_permission_code:
            if hasattr(self.source_permission_code, 'to_alipay_dict'):
                params['source_permission_code'] = self.source_permission_code.to_alipay_dict()
            else:
                params['source_permission_code'] = self.source_permission_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessPermission()
        if 'domain' in d:
            o.domain = d['domain']
        if 'permission_code' in d:
            o.permission_code = d['permission_code']
        if 'source_permission_code' in d:
            o.source_permission_code = d['source_permission_code']
        return o


