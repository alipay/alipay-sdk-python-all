#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SelfSignInfo(object):

    def __init__(self):
        self._signature = None
        self._time_stamp = None
        self._vm_id = None

    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self._signature = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value
    @property
    def vm_id(self):
        return self._vm_id

    @vm_id.setter
    def vm_id(self, value):
        self._vm_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.signature:
            if hasattr(self.signature, 'to_alipay_dict'):
                params['signature'] = self.signature.to_alipay_dict()
            else:
                params['signature'] = self.signature
        if self.time_stamp:
            if hasattr(self.time_stamp, 'to_alipay_dict'):
                params['time_stamp'] = self.time_stamp.to_alipay_dict()
            else:
                params['time_stamp'] = self.time_stamp
        if self.vm_id:
            if hasattr(self.vm_id, 'to_alipay_dict'):
                params['vm_id'] = self.vm_id.to_alipay_dict()
            else:
                params['vm_id'] = self.vm_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SelfSignInfo()
        if 'signature' in d:
            o.signature = d['signature']
        if 'time_stamp' in d:
            o.time_stamp = d['time_stamp']
        if 'vm_id' in d:
            o.vm_id = d['vm_id']
        return o


