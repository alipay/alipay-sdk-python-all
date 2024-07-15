#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockDarwinQueryModel(object):

    def __init__(self):
        self._agreement_no = None
        self._scenario = None
        self._trace = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def scenario(self):
        return self._scenario

    @scenario.setter
    def scenario(self, value):
        self._scenario = value
    @property
    def trace(self):
        return self._trace

    @trace.setter
    def trace(self, value):
        self._trace = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.scenario:
            if hasattr(self.scenario, 'to_alipay_dict'):
                params['scenario'] = self.scenario.to_alipay_dict()
            else:
                params['scenario'] = self.scenario
        if self.trace:
            if hasattr(self.trace, 'to_alipay_dict'):
                params['trace'] = self.trace.to_alipay_dict()
            else:
                params['trace'] = self.trace
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockDarwinQueryModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'scenario' in d:
            o.scenario = d['scenario']
        if 'trace' in d:
            o.trace = d['trace']
        return o


