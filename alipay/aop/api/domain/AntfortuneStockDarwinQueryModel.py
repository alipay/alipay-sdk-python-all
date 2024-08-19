#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockDarwinQueryModel(object):

    def __init__(self):
        self._agreement_no = None
        self._crowd_id = None
        self._scenario = None
        self._trace = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
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
        if self.crowd_id:
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
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
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'scenario' in d:
            o.scenario = d['scenario']
        if 'trace' in d:
            o.trace = d['trace']
        return o


