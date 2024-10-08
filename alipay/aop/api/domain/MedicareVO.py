#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicareVO(object):

    def __init__(self):
        self._mi_personal_amount = None
        self._mi_pool_amount = None
        self._mi_self_amount = None

    @property
    def mi_personal_amount(self):
        return self._mi_personal_amount

    @mi_personal_amount.setter
    def mi_personal_amount(self, value):
        self._mi_personal_amount = value
    @property
    def mi_pool_amount(self):
        return self._mi_pool_amount

    @mi_pool_amount.setter
    def mi_pool_amount(self, value):
        self._mi_pool_amount = value
    @property
    def mi_self_amount(self):
        return self._mi_self_amount

    @mi_self_amount.setter
    def mi_self_amount(self, value):
        self._mi_self_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.mi_personal_amount:
            if hasattr(self.mi_personal_amount, 'to_alipay_dict'):
                params['mi_personal_amount'] = self.mi_personal_amount.to_alipay_dict()
            else:
                params['mi_personal_amount'] = self.mi_personal_amount
        if self.mi_pool_amount:
            if hasattr(self.mi_pool_amount, 'to_alipay_dict'):
                params['mi_pool_amount'] = self.mi_pool_amount.to_alipay_dict()
            else:
                params['mi_pool_amount'] = self.mi_pool_amount
        if self.mi_self_amount:
            if hasattr(self.mi_self_amount, 'to_alipay_dict'):
                params['mi_self_amount'] = self.mi_self_amount.to_alipay_dict()
            else:
                params['mi_self_amount'] = self.mi_self_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicareVO()
        if 'mi_personal_amount' in d:
            o.mi_personal_amount = d['mi_personal_amount']
        if 'mi_pool_amount' in d:
            o.mi_pool_amount = d['mi_pool_amount']
        if 'mi_self_amount' in d:
            o.mi_self_amount = d['mi_self_amount']
        return o


