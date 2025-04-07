#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainysComplexRefSeventh(object):

    def __init__(self):
        self._case_1 = None
        self._case_2 = None
        self._demo_case = None
        self._open_id = None

    @property
    def case_1(self):
        return self._case_1

    @case_1.setter
    def case_1(self, value):
        self._case_1 = value
    @property
    def case_2(self):
        return self._case_2

    @case_2.setter
    def case_2(self, value):
        self._case_2 = value
    @property
    def demo_case(self):
        return self._demo_case

    @demo_case.setter
    def demo_case(self, value):
        self._demo_case = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_1:
            if hasattr(self.case_1, 'to_alipay_dict'):
                params['case_1'] = self.case_1.to_alipay_dict()
            else:
                params['case_1'] = self.case_1
        if self.case_2:
            if hasattr(self.case_2, 'to_alipay_dict'):
                params['case_2'] = self.case_2.to_alipay_dict()
            else:
                params['case_2'] = self.case_2
        if self.demo_case:
            if hasattr(self.demo_case, 'to_alipay_dict'):
                params['demo_case'] = self.demo_case.to_alipay_dict()
            else:
                params['demo_case'] = self.demo_case
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainysComplexRefSeventh()
        if 'case_1' in d:
            o.case_1 = d['case_1']
        if 'case_2' in d:
            o.case_2 = d['case_2']
        if 'demo_case' in d:
            o.demo_case = d['demo_case']
        if 'open_id' in d:
            o.open_id = d['open_id']
        return o


