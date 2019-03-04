#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MachineType(object):

    def __init__(self):
        self._machine_type_id = None
        self._remark = None
        self._status = None

    @property
    def machine_type_id(self):
        return self._machine_type_id

    @machine_type_id.setter
    def machine_type_id(self, value):
        self._machine_type_id = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.machine_type_id:
            if hasattr(self.machine_type_id, 'to_alipay_dict'):
                params['machine_type_id'] = self.machine_type_id.to_alipay_dict()
            else:
                params['machine_type_id'] = self.machine_type_id
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
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
        o = MachineType()
        if 'machine_type_id' in d:
            o.machine_type_id = d['machine_type_id']
        if 'remark' in d:
            o.remark = d['remark']
        if 'status' in d:
            o.status = d['status']
        return o


