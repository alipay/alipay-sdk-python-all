#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CouponInfo(object):

    def __init__(self):
        self._benefit_id = None
        self._benefit_type = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def benefit_type(self):
        return self._benefit_type

    @benefit_type.setter
    def benefit_type(self, value):
        self._benefit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.benefit_type:
            if hasattr(self.benefit_type, 'to_alipay_dict'):
                params['benefit_type'] = self.benefit_type.to_alipay_dict()
            else:
                params['benefit_type'] = self.benefit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CouponInfo()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'benefit_type' in d:
            o.benefit_type = d['benefit_type']
        return o


