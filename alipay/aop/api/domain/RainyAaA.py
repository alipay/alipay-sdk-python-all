#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyWeakRefFourth import RainyWeakRefFourth


class RainyAaA(object):

    def __init__(self):
        self._ref_weak = None

    @property
    def ref_weak(self):
        return self._ref_weak

    @ref_weak.setter
    def ref_weak(self, value):
        if isinstance(value, RainyWeakRefFourth):
            self._ref_weak = value
        else:
            self._ref_weak = RainyWeakRefFourth.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ref_weak:
            if hasattr(self.ref_weak, 'to_alipay_dict'):
                params['ref_weak'] = self.ref_weak.to_alipay_dict()
            else:
                params['ref_weak'] = self.ref_weak
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyAaA()
        if 'ref_weak' in d:
            o.ref_weak = d['ref_weak']
        return o


