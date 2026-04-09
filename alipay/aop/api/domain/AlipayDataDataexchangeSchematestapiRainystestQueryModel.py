#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesRefWeakFirst import RainyComplexTypesRefWeakFirst
from alipay.aop.api.domain.RainyComplexTypesRefWeakFirst import RainyComplexTypesRefWeakFirst


class AlipayDataDataexchangeSchematestapiRainystestQueryModel(object):

    def __init__(self):
        self._demo_ref = None
        self._demo_ref_no = None

    @property
    def demo_ref(self):
        return self._demo_ref

    @demo_ref.setter
    def demo_ref(self, value):
        if isinstance(value, RainyComplexTypesRefWeakFirst):
            self._demo_ref = value
        else:
            self._demo_ref = RainyComplexTypesRefWeakFirst.from_alipay_dict(value)
    @property
    def demo_ref_no(self):
        return self._demo_ref_no

    @demo_ref_no.setter
    def demo_ref_no(self, value):
        if isinstance(value, list):
            self._demo_ref_no = list()
            for i in value:
                if isinstance(i, RainyComplexTypesRefWeakFirst):
                    self._demo_ref_no.append(i)
                else:
                    self._demo_ref_no.append(RainyComplexTypesRefWeakFirst.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.demo_ref:
            if hasattr(self.demo_ref, 'to_alipay_dict'):
                params['demo_ref'] = self.demo_ref.to_alipay_dict()
            else:
                params['demo_ref'] = self.demo_ref
        if self.demo_ref_no:
            if isinstance(self.demo_ref_no, list):
                for i in range(0, len(self.demo_ref_no)):
                    element = self.demo_ref_no[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.demo_ref_no[i] = element.to_alipay_dict()
            if hasattr(self.demo_ref_no, 'to_alipay_dict'):
                params['demo_ref_no'] = self.demo_ref_no.to_alipay_dict()
            else:
                params['demo_ref_no'] = self.demo_ref_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataexchangeSchematestapiRainystestQueryModel()
        if 'demo_ref' in d:
            o.demo_ref = d['demo_ref']
        if 'demo_ref_no' in d:
            o.demo_ref_no = d['demo_ref_no']
        return o


