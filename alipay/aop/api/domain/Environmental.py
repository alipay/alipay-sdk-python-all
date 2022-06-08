#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Environmental(object):

    def __init__(self):
        self._energy_amount = None
        self._environmental = None

    @property
    def energy_amount(self):
        return self._energy_amount

    @energy_amount.setter
    def energy_amount(self, value):
        self._energy_amount = value
    @property
    def environmental(self):
        return self._environmental

    @environmental.setter
    def environmental(self, value):
        self._environmental = value


    def to_alipay_dict(self):
        params = dict()
        if self.energy_amount:
            if hasattr(self.energy_amount, 'to_alipay_dict'):
                params['energy_amount'] = self.energy_amount.to_alipay_dict()
            else:
                params['energy_amount'] = self.energy_amount
        if self.environmental:
            if hasattr(self.environmental, 'to_alipay_dict'):
                params['environmental'] = self.environmental.to_alipay_dict()
            else:
                params['environmental'] = self.environmental
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Environmental()
        if 'energy_amount' in d:
            o.energy_amount = d['energy_amount']
        if 'environmental' in d:
            o.environmental = d['environmental']
        return o


