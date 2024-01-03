#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCarFreeCancelRule(object):

    def __init__(self):
        self._free_date = None
        self._free_minutes = None
        self._free_type = None

    @property
    def free_date(self):
        return self._free_date

    @free_date.setter
    def free_date(self, value):
        self._free_date = value
    @property
    def free_minutes(self):
        return self._free_minutes

    @free_minutes.setter
    def free_minutes(self, value):
        self._free_minutes = value
    @property
    def free_type(self):
        return self._free_type

    @free_type.setter
    def free_type(self, value):
        self._free_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.free_date:
            if hasattr(self.free_date, 'to_alipay_dict'):
                params['free_date'] = self.free_date.to_alipay_dict()
            else:
                params['free_date'] = self.free_date
        if self.free_minutes:
            if hasattr(self.free_minutes, 'to_alipay_dict'):
                params['free_minutes'] = self.free_minutes.to_alipay_dict()
            else:
                params['free_minutes'] = self.free_minutes
        if self.free_type:
            if hasattr(self.free_type, 'to_alipay_dict'):
                params['free_type'] = self.free_type.to_alipay_dict()
            else:
                params['free_type'] = self.free_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCarFreeCancelRule()
        if 'free_date' in d:
            o.free_date = d['free_date']
        if 'free_minutes' in d:
            o.free_minutes = d['free_minutes']
        if 'free_type' in d:
            o.free_type = d['free_type']
        return o


