#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoyagerPaymentMethod(object):

    def __init__(self):
        self._payment_method_type = None

    @property
    def payment_method_type(self):
        return self._payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self._payment_method_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.payment_method_type:
            if hasattr(self.payment_method_type, 'to_alipay_dict'):
                params['payment_method_type'] = self.payment_method_type.to_alipay_dict()
            else:
                params['payment_method_type'] = self.payment_method_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerPaymentMethod()
        if 'payment_method_type' in d:
            o.payment_method_type = d['payment_method_type']
        return o


