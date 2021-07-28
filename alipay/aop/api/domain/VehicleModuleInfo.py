#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehicleModuleInfo(object):

    def __init__(self):
        self._desc = None
        self._function = None
        self._status = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, value):
        self._function = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.function:
            if hasattr(self.function, 'to_alipay_dict'):
                params['function'] = self.function.to_alipay_dict()
            else:
                params['function'] = self.function
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehicleModuleInfo()
        if 'desc' in d:
            o.desc = d['desc']
        if 'function' in d:
            o.function = d['function']
        if 'status' in d:
            o.status = d['status']
        return o


