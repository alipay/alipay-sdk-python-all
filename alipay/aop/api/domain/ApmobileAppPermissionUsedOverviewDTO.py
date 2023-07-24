#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApmobileAppPermissionUsedOverviewDTO(object):

    def __init__(self):
        self._permission_code = None
        self._permission_name = None
        self._permission_type = None

    @property
    def permission_code(self):
        return self._permission_code

    @permission_code.setter
    def permission_code(self, value):
        self._permission_code = value
    @property
    def permission_name(self):
        return self._permission_name

    @permission_name.setter
    def permission_name(self, value):
        self._permission_name = value
    @property
    def permission_type(self):
        return self._permission_type

    @permission_type.setter
    def permission_type(self, value):
        self._permission_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.permission_code:
            if hasattr(self.permission_code, 'to_alipay_dict'):
                params['permission_code'] = self.permission_code.to_alipay_dict()
            else:
                params['permission_code'] = self.permission_code
        if self.permission_name:
            if hasattr(self.permission_name, 'to_alipay_dict'):
                params['permission_name'] = self.permission_name.to_alipay_dict()
            else:
                params['permission_name'] = self.permission_name
        if self.permission_type:
            if hasattr(self.permission_type, 'to_alipay_dict'):
                params['permission_type'] = self.permission_type.to_alipay_dict()
            else:
                params['permission_type'] = self.permission_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileAppPermissionUsedOverviewDTO()
        if 'permission_code' in d:
            o.permission_code = d['permission_code']
        if 'permission_name' in d:
            o.permission_name = d['permission_name']
        if 'permission_type' in d:
            o.permission_type = d['permission_type']
        return o


