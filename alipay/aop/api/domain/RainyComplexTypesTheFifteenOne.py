#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFourth import RainyComplexTypesTheFourth


class RainyComplexTypesTheFifteenOne(object):

    def __init__(self):
        self._open_id = None
        self._weak_ref = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def weak_ref(self):
        return self._weak_ref

    @weak_ref.setter
    def weak_ref(self, value):
        if isinstance(value, list):
            self._weak_ref = list()
            for i in value:
                if isinstance(i, RainyComplexTypesTheFourth):
                    self._weak_ref.append(i)
                else:
                    self._weak_ref.append(RainyComplexTypesTheFourth.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.weak_ref:
            if isinstance(self.weak_ref, list):
                for i in range(0, len(self.weak_ref)):
                    element = self.weak_ref[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.weak_ref[i] = element.to_alipay_dict()
            if hasattr(self.weak_ref, 'to_alipay_dict'):
                params['weak_ref'] = self.weak_ref.to_alipay_dict()
            else:
                params['weak_ref'] = self.weak_ref
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyComplexTypesTheFifteenOne()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'weak_ref' in d:
            o.weak_ref = d['weak_ref']
        return o


