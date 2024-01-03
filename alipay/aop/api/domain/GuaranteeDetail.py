#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GuaranteeDetail(object):

    def __init__(self):
        self._all_free = None
        self._limit_amount = None

    @property
    def all_free(self):
        return self._all_free

    @all_free.setter
    def all_free(self, value):
        self._all_free = value
    @property
    def limit_amount(self):
        return self._limit_amount

    @limit_amount.setter
    def limit_amount(self, value):
        self._limit_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.all_free:
            if hasattr(self.all_free, 'to_alipay_dict'):
                params['all_free'] = self.all_free.to_alipay_dict()
            else:
                params['all_free'] = self.all_free
        if self.limit_amount:
            if hasattr(self.limit_amount, 'to_alipay_dict'):
                params['limit_amount'] = self.limit_amount.to_alipay_dict()
            else:
                params['limit_amount'] = self.limit_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GuaranteeDetail()
        if 'all_free' in d:
            o.all_free = d['all_free']
        if 'limit_amount' in d:
            o.limit_amount = d['limit_amount']
        return o


