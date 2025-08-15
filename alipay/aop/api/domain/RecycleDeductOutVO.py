#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleDeductOutVO(object):

    def __init__(self):
        self._deduct_out = None
        self._deduct_out_open_id = None
        self._deduct_out_type = None
        self._deduct_pid = None
        self._deduct_pid_open_id = None

    @property
    def deduct_out(self):
        return self._deduct_out

    @deduct_out.setter
    def deduct_out(self, value):
        self._deduct_out = value
    @property
    def deduct_out_open_id(self):
        return self._deduct_out_open_id

    @deduct_out_open_id.setter
    def deduct_out_open_id(self, value):
        self._deduct_out_open_id = value
    @property
    def deduct_out_type(self):
        return self._deduct_out_type

    @deduct_out_type.setter
    def deduct_out_type(self, value):
        self._deduct_out_type = value
    @property
    def deduct_pid(self):
        return self._deduct_pid

    @deduct_pid.setter
    def deduct_pid(self, value):
        self._deduct_pid = value
    @property
    def deduct_pid_open_id(self):
        return self._deduct_pid_open_id

    @deduct_pid_open_id.setter
    def deduct_pid_open_id(self, value):
        self._deduct_pid_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduct_out:
            if hasattr(self.deduct_out, 'to_alipay_dict'):
                params['deduct_out'] = self.deduct_out.to_alipay_dict()
            else:
                params['deduct_out'] = self.deduct_out
        if self.deduct_out_open_id:
            if hasattr(self.deduct_out_open_id, 'to_alipay_dict'):
                params['deduct_out_open_id'] = self.deduct_out_open_id.to_alipay_dict()
            else:
                params['deduct_out_open_id'] = self.deduct_out_open_id
        if self.deduct_out_type:
            if hasattr(self.deduct_out_type, 'to_alipay_dict'):
                params['deduct_out_type'] = self.deduct_out_type.to_alipay_dict()
            else:
                params['deduct_out_type'] = self.deduct_out_type
        if self.deduct_pid:
            if hasattr(self.deduct_pid, 'to_alipay_dict'):
                params['deduct_pid'] = self.deduct_pid.to_alipay_dict()
            else:
                params['deduct_pid'] = self.deduct_pid
        if self.deduct_pid_open_id:
            if hasattr(self.deduct_pid_open_id, 'to_alipay_dict'):
                params['deduct_pid_open_id'] = self.deduct_pid_open_id.to_alipay_dict()
            else:
                params['deduct_pid_open_id'] = self.deduct_pid_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleDeductOutVO()
        if 'deduct_out' in d:
            o.deduct_out = d['deduct_out']
        if 'deduct_out_open_id' in d:
            o.deduct_out_open_id = d['deduct_out_open_id']
        if 'deduct_out_type' in d:
            o.deduct_out_type = d['deduct_out_type']
        if 'deduct_pid' in d:
            o.deduct_pid = d['deduct_pid']
        if 'deduct_pid_open_id' in d:
            o.deduct_pid_open_id = d['deduct_pid_open_id']
        return o


