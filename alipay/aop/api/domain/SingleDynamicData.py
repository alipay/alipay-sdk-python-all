#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SingleDynamicData(object):

    def __init__(self):
        self._expire = None
        self._ext_param = None
        self._priority = None
        self._unique_id = None

    @property
    def expire(self):
        return self._expire

    @expire.setter
    def expire(self, value):
        self._expire = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.expire:
            if hasattr(self.expire, 'to_alipay_dict'):
                params['expire'] = self.expire.to_alipay_dict()
            else:
                params['expire'] = self.expire
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SingleDynamicData()
        if 'expire' in d:
            o.expire = d['expire']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'priority' in d:
            o.priority = d['priority']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


