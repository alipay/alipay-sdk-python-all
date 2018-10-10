#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbpFundTool(object):

    def __init__(self):
        self._f_fee = None
        self._f_id = None
        self._f_type = None

    @property
    def f_fee(self):
        return self._f_fee

    @f_fee.setter
    def f_fee(self, value):
        self._f_fee = value
    @property
    def f_id(self):
        return self._f_id

    @f_id.setter
    def f_id(self, value):
        self._f_id = value
    @property
    def f_type(self):
        return self._f_type

    @f_type.setter
    def f_type(self, value):
        self._f_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.f_fee:
            if hasattr(self.f_fee, 'to_alipay_dict'):
                params['f_fee'] = self.f_fee.to_alipay_dict()
            else:
                params['f_fee'] = self.f_fee
        if self.f_id:
            if hasattr(self.f_id, 'to_alipay_dict'):
                params['f_id'] = self.f_id.to_alipay_dict()
            else:
                params['f_id'] = self.f_id
        if self.f_type:
            if hasattr(self.f_type, 'to_alipay_dict'):
                params['f_type'] = self.f_type.to_alipay_dict()
            else:
                params['f_type'] = self.f_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbpFundTool()
        if 'f_fee' in d:
            o.f_fee = d['f_fee']
        if 'f_id' in d:
            o.f_id = d['f_id']
        if 'f_type' in d:
            o.f_type = d['f_type']
        return o


