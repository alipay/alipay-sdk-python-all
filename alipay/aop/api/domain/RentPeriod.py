#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPeriod(object):

    def __init__(self):
        self._step = None
        self._total = None
        self._unit = None

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.step:
            if hasattr(self.step, 'to_alipay_dict'):
                params['step'] = self.step.to_alipay_dict()
            else:
                params['step'] = self.step
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPeriod()
        if 'step' in d:
            o.step = d['step']
        if 'total' in d:
            o.total = d['total']
        if 'unit' in d:
            o.unit = d['unit']
        return o


