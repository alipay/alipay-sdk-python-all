#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryOfflinelaborRegisterModifyModel(object):

    def __init__(self):
        self._apply_status = None
        self._hire_time = None
        self._out_register_id = None

    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def hire_time(self):
        return self._hire_time

    @hire_time.setter
    def hire_time(self, value):
        self._hire_time = value
    @property
    def out_register_id(self):
        return self._out_register_id

    @out_register_id.setter
    def out_register_id(self, value):
        self._out_register_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.hire_time:
            if hasattr(self.hire_time, 'to_alipay_dict'):
                params['hire_time'] = self.hire_time.to_alipay_dict()
            else:
                params['hire_time'] = self.hire_time
        if self.out_register_id:
            if hasattr(self.out_register_id, 'to_alipay_dict'):
                params['out_register_id'] = self.out_register_id.to_alipay_dict()
            else:
                params['out_register_id'] = self.out_register_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryOfflinelaborRegisterModifyModel()
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'hire_time' in d:
            o.hire_time = d['hire_time']
        if 'out_register_id' in d:
            o.out_register_id = d['out_register_id']
        return o


