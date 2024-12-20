#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesRefWeakFirst import RainyComplexTypesRefWeakFirst
from alipay.aop.api.domain.RainyComplexTypesRefWeakSecond import RainyComplexTypesRefWeakSecond


class AlipayDataDataserviceSchemacomplexthirdRainystestQueryModel(object):

    def __init__(self):
        self._demo_new_strong = None
        self._demo_new_weak = None

    @property
    def demo_new_strong(self):
        return self._demo_new_strong

    @demo_new_strong.setter
    def demo_new_strong(self, value):
        if isinstance(value, RainyComplexTypesRefWeakFirst):
            self._demo_new_strong = value
        else:
            self._demo_new_strong = RainyComplexTypesRefWeakFirst.from_alipay_dict(value)
    @property
    def demo_new_weak(self):
        return self._demo_new_weak

    @demo_new_weak.setter
    def demo_new_weak(self, value):
        if isinstance(value, RainyComplexTypesRefWeakSecond):
            self._demo_new_weak = value
        else:
            self._demo_new_weak = RainyComplexTypesRefWeakSecond.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.demo_new_strong:
            if hasattr(self.demo_new_strong, 'to_alipay_dict'):
                params['demo_new_strong'] = self.demo_new_strong.to_alipay_dict()
            else:
                params['demo_new_strong'] = self.demo_new_strong
        if self.demo_new_weak:
            if hasattr(self.demo_new_weak, 'to_alipay_dict'):
                params['demo_new_weak'] = self.demo_new_weak.to_alipay_dict()
            else:
                params['demo_new_weak'] = self.demo_new_weak
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceSchemacomplexthirdRainystestQueryModel()
        if 'demo_new_strong' in d:
            o.demo_new_strong = d['demo_new_strong']
        if 'demo_new_weak' in d:
            o.demo_new_weak = d['demo_new_weak']
        return o


