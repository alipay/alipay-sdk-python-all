#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicineInfo(object):

    def __init__(self):
        self._consumed_time = None
        self._medicine_name = None
        self._medicine_num = None
        self._medicine_verified = None

    @property
    def consumed_time(self):
        return self._consumed_time

    @consumed_time.setter
    def consumed_time(self, value):
        self._consumed_time = value
    @property
    def medicine_name(self):
        return self._medicine_name

    @medicine_name.setter
    def medicine_name(self, value):
        self._medicine_name = value
    @property
    def medicine_num(self):
        return self._medicine_num

    @medicine_num.setter
    def medicine_num(self, value):
        self._medicine_num = value
    @property
    def medicine_verified(self):
        return self._medicine_verified

    @medicine_verified.setter
    def medicine_verified(self, value):
        self._medicine_verified = value


    def to_alipay_dict(self):
        params = dict()
        if self.consumed_time:
            if hasattr(self.consumed_time, 'to_alipay_dict'):
                params['consumed_time'] = self.consumed_time.to_alipay_dict()
            else:
                params['consumed_time'] = self.consumed_time
        if self.medicine_name:
            if hasattr(self.medicine_name, 'to_alipay_dict'):
                params['medicine_name'] = self.medicine_name.to_alipay_dict()
            else:
                params['medicine_name'] = self.medicine_name
        if self.medicine_num:
            if hasattr(self.medicine_num, 'to_alipay_dict'):
                params['medicine_num'] = self.medicine_num.to_alipay_dict()
            else:
                params['medicine_num'] = self.medicine_num
        if self.medicine_verified:
            if hasattr(self.medicine_verified, 'to_alipay_dict'):
                params['medicine_verified'] = self.medicine_verified.to_alipay_dict()
            else:
                params['medicine_verified'] = self.medicine_verified
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicineInfo()
        if 'consumed_time' in d:
            o.consumed_time = d['consumed_time']
        if 'medicine_name' in d:
            o.medicine_name = d['medicine_name']
        if 'medicine_num' in d:
            o.medicine_num = d['medicine_num']
        if 'medicine_verified' in d:
            o.medicine_verified = d['medicine_verified']
        return o


