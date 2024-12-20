#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyAaA import RainyAaA
from alipay.aop.api.domain.RainyComplexTypesRefWeakFirst import RainyComplexTypesRefWeakFirst


class RainyAa(object):

    def __init__(self):
        self._object_weak = None
        self._ref_strong = None

    @property
    def object_weak(self):
        return self._object_weak

    @object_weak.setter
    def object_weak(self, value):
        if isinstance(value, RainyAaA):
            self._object_weak = value
        else:
            self._object_weak = RainyAaA.from_alipay_dict(value)
    @property
    def ref_strong(self):
        return self._ref_strong

    @ref_strong.setter
    def ref_strong(self, value):
        if isinstance(value, RainyComplexTypesRefWeakFirst):
            self._ref_strong = value
        else:
            self._ref_strong = RainyComplexTypesRefWeakFirst.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.object_weak:
            if hasattr(self.object_weak, 'to_alipay_dict'):
                params['object_weak'] = self.object_weak.to_alipay_dict()
            else:
                params['object_weak'] = self.object_weak
        if self.ref_strong:
            if hasattr(self.ref_strong, 'to_alipay_dict'):
                params['ref_strong'] = self.ref_strong.to_alipay_dict()
            else:
                params['ref_strong'] = self.ref_strong
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyAa()
        if 'object_weak' in d:
            o.object_weak = d['object_weak']
        if 'ref_strong' in d:
            o.ref_strong = d['ref_strong']
        return o


