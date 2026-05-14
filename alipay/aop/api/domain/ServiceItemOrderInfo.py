#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceItemOrderInfo(object):

    def __init__(self):
        self._bill_end_time = None
        self._bill_start_time = None
        self._patient_name = None

    @property
    def bill_end_time(self):
        return self._bill_end_time

    @bill_end_time.setter
    def bill_end_time(self, value):
        self._bill_end_time = value
    @property
    def bill_start_time(self):
        return self._bill_start_time

    @bill_start_time.setter
    def bill_start_time(self, value):
        self._bill_start_time = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_end_time:
            if hasattr(self.bill_end_time, 'to_alipay_dict'):
                params['bill_end_time'] = self.bill_end_time.to_alipay_dict()
            else:
                params['bill_end_time'] = self.bill_end_time
        if self.bill_start_time:
            if hasattr(self.bill_start_time, 'to_alipay_dict'):
                params['bill_start_time'] = self.bill_start_time.to_alipay_dict()
            else:
                params['bill_start_time'] = self.bill_start_time
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceItemOrderInfo()
        if 'bill_end_time' in d:
            o.bill_end_time = d['bill_end_time']
        if 'bill_start_time' in d:
            o.bill_start_time = d['bill_start_time']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        return o


