#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContributeDetail(object):

    def __init__(self):
        self._contribute_amount = None
        self._contribute_type = None

    @property
    def contribute_amount(self):
        return self._contribute_amount

    @contribute_amount.setter
    def contribute_amount(self, value):
        self._contribute_amount = value
    @property
    def contribute_type(self):
        return self._contribute_type

    @contribute_type.setter
    def contribute_type(self, value):
        self._contribute_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.contribute_amount:
            if hasattr(self.contribute_amount, 'to_alipay_dict'):
                params['contribute_amount'] = self.contribute_amount.to_alipay_dict()
            else:
                params['contribute_amount'] = self.contribute_amount
        if self.contribute_type:
            if hasattr(self.contribute_type, 'to_alipay_dict'):
                params['contribute_type'] = self.contribute_type.to_alipay_dict()
            else:
                params['contribute_type'] = self.contribute_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContributeDetail()
        if 'contribute_amount' in d:
            o.contribute_amount = d['contribute_amount']
        if 'contribute_type' in d:
            o.contribute_type = d['contribute_type']
        return o


