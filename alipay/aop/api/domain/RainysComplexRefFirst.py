#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainysComplexRefFirst(object):

    def __init__(self):
        self._case_string = None

    @property
    def case_string(self):
        return self._case_string

    @case_string.setter
    def case_string(self, value):
        self._case_string = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_string:
            if hasattr(self.case_string, 'to_alipay_dict'):
                params['case_string'] = self.case_string.to_alipay_dict()
            else:
                params['case_string'] = self.case_string
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainysComplexRefFirst()
        if 'case_string' in d:
            o.case_string = d['case_string']
        return o


