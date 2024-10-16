#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TapPayInfo(object):

    def __init__(self):
        self._payment_medium_type = None

    @property
    def payment_medium_type(self):
        return self._payment_medium_type

    @payment_medium_type.setter
    def payment_medium_type(self, value):
        self._payment_medium_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.payment_medium_type:
            if hasattr(self.payment_medium_type, 'to_alipay_dict'):
                params['payment_medium_type'] = self.payment_medium_type.to_alipay_dict()
            else:
                params['payment_medium_type'] = self.payment_medium_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TapPayInfo()
        if 'payment_medium_type' in d:
            o.payment_medium_type = d['payment_medium_type']
        return o


