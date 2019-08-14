#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndirectIsvInfo(object):

    def __init__(self):
        self._is_ts_binding = None
        self._isv_name = None
        self._isv_pid = None

    @property
    def is_ts_binding(self):
        return self._is_ts_binding

    @is_ts_binding.setter
    def is_ts_binding(self, value):
        self._is_ts_binding = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_ts_binding:
            if hasattr(self.is_ts_binding, 'to_alipay_dict'):
                params['is_ts_binding'] = self.is_ts_binding.to_alipay_dict()
            else:
                params['is_ts_binding'] = self.is_ts_binding
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndirectIsvInfo()
        if 'is_ts_binding' in d:
            o.is_ts_binding = d['is_ts_binding']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        return o


