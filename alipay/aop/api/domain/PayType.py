#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayType(object):

    def __init__(self):
        self._payer_bank_type = None

    @property
    def payer_bank_type(self):
        return self._payer_bank_type

    @payer_bank_type.setter
    def payer_bank_type(self, value):
        self._payer_bank_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.payer_bank_type:
            if hasattr(self.payer_bank_type, 'to_alipay_dict'):
                params['payer_bank_type'] = self.payer_bank_type.to_alipay_dict()
            else:
                params['payer_bank_type'] = self.payer_bank_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayType()
        if 'payer_bank_type' in d:
            o.payer_bank_type = d['payer_bank_type']
        return o


