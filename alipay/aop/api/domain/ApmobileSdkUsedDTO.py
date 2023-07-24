#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApmobileSdkUsedDTO(object):

    def __init__(self):
        self._permission_id = None
        self._permission_name = None
        self._sdk_used_num = None

    @property
    def permission_id(self):
        return self._permission_id

    @permission_id.setter
    def permission_id(self, value):
        self._permission_id = value
    @property
    def permission_name(self):
        return self._permission_name

    @permission_name.setter
    def permission_name(self, value):
        self._permission_name = value
    @property
    def sdk_used_num(self):
        return self._sdk_used_num

    @sdk_used_num.setter
    def sdk_used_num(self, value):
        self._sdk_used_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.permission_id:
            if hasattr(self.permission_id, 'to_alipay_dict'):
                params['permission_id'] = self.permission_id.to_alipay_dict()
            else:
                params['permission_id'] = self.permission_id
        if self.permission_name:
            if hasattr(self.permission_name, 'to_alipay_dict'):
                params['permission_name'] = self.permission_name.to_alipay_dict()
            else:
                params['permission_name'] = self.permission_name
        if self.sdk_used_num:
            if hasattr(self.sdk_used_num, 'to_alipay_dict'):
                params['sdk_used_num'] = self.sdk_used_num.to_alipay_dict()
            else:
                params['sdk_used_num'] = self.sdk_used_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileSdkUsedDTO()
        if 'permission_id' in d:
            o.permission_id = d['permission_id']
        if 'permission_name' in d:
            o.permission_name = d['permission_name']
        if 'sdk_used_num' in d:
            o.sdk_used_num = d['sdk_used_num']
        return o


