#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentManualRiskDetail(object):

    def __init__(self):
        self._judge = None
        self._pass = None

    @property
    def judge(self):
        return self._judge

    @judge.setter
    def judge(self, value):
        self._judge = value
    @property
    def pass(self):
        return self._pass

    @pass.setter
    def pass(self, value):
        self._pass = value


    def to_alipay_dict(self):
        params = dict()
        if self.judge:
            if hasattr(self.judge, 'to_alipay_dict'):
                params['judge'] = self.judge.to_alipay_dict()
            else:
                params['judge'] = self.judge
        if self.pass:
            if hasattr(self.pass, 'to_alipay_dict'):
                params['pass'] = self.pass.to_alipay_dict()
            else:
                params['pass'] = self.pass
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentManualRiskDetail()
        if 'judge' in d:
            o.judge = d['judge']
        if 'pass' in d:
            o.pass = d['pass']
        return o


