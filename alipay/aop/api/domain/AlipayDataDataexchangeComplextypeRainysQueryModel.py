#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFirst import RainyComplexTypesTheFirst
from alipay.aop.api.domain.RainyComplexTypesTheSecond import RainyComplexTypesTheSecond


class AlipayDataDataexchangeComplextypeRainysQueryModel(object):

    def __init__(self):
        self._references_test_a = None
        self._references_test_b = None

    @property
    def references_test_a(self):
        return self._references_test_a

    @references_test_a.setter
    def references_test_a(self, value):
        if isinstance(value, RainyComplexTypesTheFirst):
            self._references_test_a = value
        else:
            self._references_test_a = RainyComplexTypesTheFirst.from_alipay_dict(value)
    @property
    def references_test_b(self):
        return self._references_test_b

    @references_test_b.setter
    def references_test_b(self, value):
        if isinstance(value, RainyComplexTypesTheSecond):
            self._references_test_b = value
        else:
            self._references_test_b = RainyComplexTypesTheSecond.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.references_test_a:
            if hasattr(self.references_test_a, 'to_alipay_dict'):
                params['references_test_a'] = self.references_test_a.to_alipay_dict()
            else:
                params['references_test_a'] = self.references_test_a
        if self.references_test_b:
            if hasattr(self.references_test_b, 'to_alipay_dict'):
                params['references_test_b'] = self.references_test_b.to_alipay_dict()
            else:
                params['references_test_b'] = self.references_test_b
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataexchangeComplextypeRainysQueryModel()
        if 'references_test_a' in d:
            o.references_test_a = d['references_test_a']
        if 'references_test_b' in d:
            o.references_test_b = d['references_test_b']
        return o


