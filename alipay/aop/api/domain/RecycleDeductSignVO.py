#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleDeductSignVO(object):

    def __init__(self):
        self._deduct_sign_pid = None
        self._deduct_sign_status = None
        self._deduct_sign_type = None

    @property
    def deduct_sign_pid(self):
        return self._deduct_sign_pid

    @deduct_sign_pid.setter
    def deduct_sign_pid(self, value):
        self._deduct_sign_pid = value
    @property
    def deduct_sign_status(self):
        return self._deduct_sign_status

    @deduct_sign_status.setter
    def deduct_sign_status(self, value):
        self._deduct_sign_status = value
    @property
    def deduct_sign_type(self):
        return self._deduct_sign_type

    @deduct_sign_type.setter
    def deduct_sign_type(self, value):
        self._deduct_sign_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduct_sign_pid:
            if hasattr(self.deduct_sign_pid, 'to_alipay_dict'):
                params['deduct_sign_pid'] = self.deduct_sign_pid.to_alipay_dict()
            else:
                params['deduct_sign_pid'] = self.deduct_sign_pid
        if self.deduct_sign_status:
            if hasattr(self.deduct_sign_status, 'to_alipay_dict'):
                params['deduct_sign_status'] = self.deduct_sign_status.to_alipay_dict()
            else:
                params['deduct_sign_status'] = self.deduct_sign_status
        if self.deduct_sign_type:
            if hasattr(self.deduct_sign_type, 'to_alipay_dict'):
                params['deduct_sign_type'] = self.deduct_sign_type.to_alipay_dict()
            else:
                params['deduct_sign_type'] = self.deduct_sign_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleDeductSignVO()
        if 'deduct_sign_pid' in d:
            o.deduct_sign_pid = d['deduct_sign_pid']
        if 'deduct_sign_status' in d:
            o.deduct_sign_status = d['deduct_sign_status']
        if 'deduct_sign_type' in d:
            o.deduct_sign_type = d['deduct_sign_type']
        return o


