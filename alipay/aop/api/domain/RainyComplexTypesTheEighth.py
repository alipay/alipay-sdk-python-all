#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainyComplexTypesTheEighth(object):

    def __init__(self):
        self._case_string = None
        self._demo_case = None

    @property
    def case_string(self):
        return self._case_string

    @case_string.setter
    def case_string(self, value):
        self._case_string = value
    @property
    def demo_case(self):
        return self._demo_case

    @demo_case.setter
    def demo_case(self, value):
        self._demo_case = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_string:
            if hasattr(self.case_string, 'to_alipay_dict'):
                params['case_string'] = self.case_string.to_alipay_dict()
            else:
                params['case_string'] = self.case_string
        if self.demo_case:
            if hasattr(self.demo_case, 'to_alipay_dict'):
                params['demo_case'] = self.demo_case.to_alipay_dict()
            else:
                params['demo_case'] = self.demo_case
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyComplexTypesTheEighth()
        if 'case_string' in d:
            o.case_string = d['case_string']
        if 'demo_case' in d:
            o.demo_case = d['demo_case']
        return o


