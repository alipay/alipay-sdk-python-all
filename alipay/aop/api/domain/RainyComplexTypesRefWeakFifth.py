#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainysComplexTypeWeakRefFifth import RainysComplexTypeWeakRefFifth


class RainyComplexTypesRefWeakFifth(object):

    def __init__(self):
        self._demo_case = None
        self._demo_ref_list = None

    @property
    def demo_case(self):
        return self._demo_case

    @demo_case.setter
    def demo_case(self, value):
        self._demo_case = value
    @property
    def demo_ref_list(self):
        return self._demo_ref_list

    @demo_ref_list.setter
    def demo_ref_list(self, value):
        if isinstance(value, list):
            self._demo_ref_list = list()
            for i in value:
                if isinstance(i, RainysComplexTypeWeakRefFifth):
                    self._demo_ref_list.append(i)
                else:
                    self._demo_ref_list.append(RainysComplexTypeWeakRefFifth.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.demo_case:
            if hasattr(self.demo_case, 'to_alipay_dict'):
                params['demo_case'] = self.demo_case.to_alipay_dict()
            else:
                params['demo_case'] = self.demo_case
        if self.demo_ref_list:
            if isinstance(self.demo_ref_list, list):
                for i in range(0, len(self.demo_ref_list)):
                    element = self.demo_ref_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.demo_ref_list[i] = element.to_alipay_dict()
            if hasattr(self.demo_ref_list, 'to_alipay_dict'):
                params['demo_ref_list'] = self.demo_ref_list.to_alipay_dict()
            else:
                params['demo_ref_list'] = self.demo_ref_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyComplexTypesRefWeakFifth()
        if 'demo_case' in d:
            o.demo_case = d['demo_case']
        if 'demo_ref_list' in d:
            o.demo_ref_list = d['demo_ref_list']
        return o


