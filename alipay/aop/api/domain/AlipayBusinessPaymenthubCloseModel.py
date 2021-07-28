#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBusinessPaymenthubCloseModel(object):

    def __init__(self):
        self._payment_id = None

    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.payment_id:
            if hasattr(self.payment_id, 'to_alipay_dict'):
                params['payment_id'] = self.payment_id.to_alipay_dict()
            else:
                params['payment_id'] = self.payment_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessPaymenthubCloseModel()
        if 'payment_id' in d:
            o.payment_id = d['payment_id']
        return o


