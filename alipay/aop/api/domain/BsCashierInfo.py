#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BsCashierInfo(object):

    def __init__(self):
        self._cashier_type = None

    @property
    def cashier_type(self):
        return self._cashier_type

    @cashier_type.setter
    def cashier_type(self, value):
        self._cashier_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cashier_type:
            if hasattr(self.cashier_type, 'to_alipay_dict'):
                params['cashier_type'] = self.cashier_type.to_alipay_dict()
            else:
                params['cashier_type'] = self.cashier_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsCashierInfo()
        if 'cashier_type' in d:
            o.cashier_type = d['cashier_type']
        return o


