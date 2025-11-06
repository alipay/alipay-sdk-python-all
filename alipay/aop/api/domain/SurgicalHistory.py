#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SurgicalHistory(object):

    def __init__(self):
        self._surgery_date = None
        self._surgery_name = None

    @property
    def surgery_date(self):
        return self._surgery_date

    @surgery_date.setter
    def surgery_date(self, value):
        self._surgery_date = value
    @property
    def surgery_name(self):
        return self._surgery_name

    @surgery_name.setter
    def surgery_name(self, value):
        self._surgery_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.surgery_date:
            if hasattr(self.surgery_date, 'to_alipay_dict'):
                params['surgery_date'] = self.surgery_date.to_alipay_dict()
            else:
                params['surgery_date'] = self.surgery_date
        if self.surgery_name:
            if hasattr(self.surgery_name, 'to_alipay_dict'):
                params['surgery_name'] = self.surgery_name.to_alipay_dict()
            else:
                params['surgery_name'] = self.surgery_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SurgicalHistory()
        if 'surgery_date' in d:
            o.surgery_date = d['surgery_date']
        if 'surgery_name' in d:
            o.surgery_name = d['surgery_name']
        return o


