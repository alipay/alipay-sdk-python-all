#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheSecond import RainyComplexTypesTheSecond
from alipay.aop.api.domain.RainyComplexTypeRefWeakFirst import RainyComplexTypeRefWeakFirst
from alipay.aop.api.domain.RainyComplexTypeRefWeakSecond import RainyComplexTypeRefWeakSecond


class AlipayDataDataserviceSchemacomplextwiceRainystestQueryModel(object):

    def __init__(self):
        self._demo_strong_complextype = None
        self._demo_weak_complextype = None
        self._weak_complextype = None

    @property
    def demo_strong_complextype(self):
        return self._demo_strong_complextype

    @demo_strong_complextype.setter
    def demo_strong_complextype(self, value):
        if isinstance(value, RainyComplexTypesTheSecond):
            self._demo_strong_complextype = value
        else:
            self._demo_strong_complextype = RainyComplexTypesTheSecond.from_alipay_dict(value)
    @property
    def demo_weak_complextype(self):
        return self._demo_weak_complextype

    @demo_weak_complextype.setter
    def demo_weak_complextype(self, value):
        if isinstance(value, RainyComplexTypeRefWeakFirst):
            self._demo_weak_complextype = value
        else:
            self._demo_weak_complextype = RainyComplexTypeRefWeakFirst.from_alipay_dict(value)
    @property
    def weak_complextype(self):
        return self._weak_complextype

    @weak_complextype.setter
    def weak_complextype(self, value):
        if isinstance(value, RainyComplexTypeRefWeakSecond):
            self._weak_complextype = value
        else:
            self._weak_complextype = RainyComplexTypeRefWeakSecond.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.demo_strong_complextype:
            if hasattr(self.demo_strong_complextype, 'to_alipay_dict'):
                params['demo_strong_complextype'] = self.demo_strong_complextype.to_alipay_dict()
            else:
                params['demo_strong_complextype'] = self.demo_strong_complextype
        if self.demo_weak_complextype:
            if hasattr(self.demo_weak_complextype, 'to_alipay_dict'):
                params['demo_weak_complextype'] = self.demo_weak_complextype.to_alipay_dict()
            else:
                params['demo_weak_complextype'] = self.demo_weak_complextype
        if self.weak_complextype:
            if hasattr(self.weak_complextype, 'to_alipay_dict'):
                params['weak_complextype'] = self.weak_complextype.to_alipay_dict()
            else:
                params['weak_complextype'] = self.weak_complextype
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceSchemacomplextwiceRainystestQueryModel()
        if 'demo_strong_complextype' in d:
            o.demo_strong_complextype = d['demo_strong_complextype']
        if 'demo_weak_complextype' in d:
            o.demo_weak_complextype = d['demo_weak_complextype']
        if 'weak_complextype' in d:
            o.weak_complextype = d['weak_complextype']
        return o


