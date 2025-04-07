#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsCbddoctorStatusSyncModel(object):

    def __init__(self):
        self._inst_doctor_id = None
        self._inst_id = None
        self._operate = None

    @property
    def inst_doctor_id(self):
        return self._inst_doctor_id

    @inst_doctor_id.setter
    def inst_doctor_id(self, value):
        self._inst_doctor_id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_doctor_id:
            if hasattr(self.inst_doctor_id, 'to_alipay_dict'):
                params['inst_doctor_id'] = self.inst_doctor_id.to_alipay_dict()
            else:
                params['inst_doctor_id'] = self.inst_doctor_id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsCbddoctorStatusSyncModel()
        if 'inst_doctor_id' in d:
            o.inst_doctor_id = d['inst_doctor_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'operate' in d:
            o.operate = d['operate']
        return o


