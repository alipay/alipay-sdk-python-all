#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MachineInfo(object):

    def __init__(self):
        self._machine_count = None
        self._machine_model = None
        self._machine_type = None

    @property
    def machine_count(self):
        return self._machine_count

    @machine_count.setter
    def machine_count(self, value):
        self._machine_count = value
    @property
    def machine_model(self):
        return self._machine_model

    @machine_model.setter
    def machine_model(self, value):
        self._machine_model = value
    @property
    def machine_type(self):
        return self._machine_type

    @machine_type.setter
    def machine_type(self, value):
        self._machine_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.machine_count:
            if hasattr(self.machine_count, 'to_alipay_dict'):
                params['machine_count'] = self.machine_count.to_alipay_dict()
            else:
                params['machine_count'] = self.machine_count
        if self.machine_model:
            if hasattr(self.machine_model, 'to_alipay_dict'):
                params['machine_model'] = self.machine_model.to_alipay_dict()
            else:
                params['machine_model'] = self.machine_model
        if self.machine_type:
            if hasattr(self.machine_type, 'to_alipay_dict'):
                params['machine_type'] = self.machine_type.to_alipay_dict()
            else:
                params['machine_type'] = self.machine_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MachineInfo()
        if 'machine_count' in d:
            o.machine_count = d['machine_count']
        if 'machine_model' in d:
            o.machine_model = d['machine_model']
        if 'machine_type' in d:
            o.machine_type = d['machine_type']
        return o


