#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class McBenefitInfo(object):

    def __init__(self):
        self._benefit_code = None
        self._benefit_expire_time = None
        self._benefit_name = None
        self._benefit_open_time = None
        self._benefit_status = None
        self._benefit_total_count = None
        self._benefit_use_count = None

    @property
    def benefit_code(self):
        return self._benefit_code

    @benefit_code.setter
    def benefit_code(self, value):
        self._benefit_code = value
    @property
    def benefit_expire_time(self):
        return self._benefit_expire_time

    @benefit_expire_time.setter
    def benefit_expire_time(self, value):
        self._benefit_expire_time = value
    @property
    def benefit_name(self):
        return self._benefit_name

    @benefit_name.setter
    def benefit_name(self, value):
        self._benefit_name = value
    @property
    def benefit_open_time(self):
        return self._benefit_open_time

    @benefit_open_time.setter
    def benefit_open_time(self, value):
        self._benefit_open_time = value
    @property
    def benefit_status(self):
        return self._benefit_status

    @benefit_status.setter
    def benefit_status(self, value):
        self._benefit_status = value
    @property
    def benefit_total_count(self):
        return self._benefit_total_count

    @benefit_total_count.setter
    def benefit_total_count(self, value):
        self._benefit_total_count = value
    @property
    def benefit_use_count(self):
        return self._benefit_use_count

    @benefit_use_count.setter
    def benefit_use_count(self, value):
        self._benefit_use_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_code:
            if hasattr(self.benefit_code, 'to_alipay_dict'):
                params['benefit_code'] = self.benefit_code.to_alipay_dict()
            else:
                params['benefit_code'] = self.benefit_code
        if self.benefit_expire_time:
            if hasattr(self.benefit_expire_time, 'to_alipay_dict'):
                params['benefit_expire_time'] = self.benefit_expire_time.to_alipay_dict()
            else:
                params['benefit_expire_time'] = self.benefit_expire_time
        if self.benefit_name:
            if hasattr(self.benefit_name, 'to_alipay_dict'):
                params['benefit_name'] = self.benefit_name.to_alipay_dict()
            else:
                params['benefit_name'] = self.benefit_name
        if self.benefit_open_time:
            if hasattr(self.benefit_open_time, 'to_alipay_dict'):
                params['benefit_open_time'] = self.benefit_open_time.to_alipay_dict()
            else:
                params['benefit_open_time'] = self.benefit_open_time
        if self.benefit_status:
            if hasattr(self.benefit_status, 'to_alipay_dict'):
                params['benefit_status'] = self.benefit_status.to_alipay_dict()
            else:
                params['benefit_status'] = self.benefit_status
        if self.benefit_total_count:
            if hasattr(self.benefit_total_count, 'to_alipay_dict'):
                params['benefit_total_count'] = self.benefit_total_count.to_alipay_dict()
            else:
                params['benefit_total_count'] = self.benefit_total_count
        if self.benefit_use_count:
            if hasattr(self.benefit_use_count, 'to_alipay_dict'):
                params['benefit_use_count'] = self.benefit_use_count.to_alipay_dict()
            else:
                params['benefit_use_count'] = self.benefit_use_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = McBenefitInfo()
        if 'benefit_code' in d:
            o.benefit_code = d['benefit_code']
        if 'benefit_expire_time' in d:
            o.benefit_expire_time = d['benefit_expire_time']
        if 'benefit_name' in d:
            o.benefit_name = d['benefit_name']
        if 'benefit_open_time' in d:
            o.benefit_open_time = d['benefit_open_time']
        if 'benefit_status' in d:
            o.benefit_status = d['benefit_status']
        if 'benefit_total_count' in d:
            o.benefit_total_count = d['benefit_total_count']
        if 'benefit_use_count' in d:
            o.benefit_use_count = d['benefit_use_count']
        return o


