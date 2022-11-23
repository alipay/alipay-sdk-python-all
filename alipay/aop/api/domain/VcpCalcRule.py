#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VcpCalcCondition import VcpCalcCondition
from alipay.aop.api.domain.VcpCalcFormula import VcpCalcFormula


class VcpCalcRule(object):

    def __init__(self):
        self._calc_condition = None
        self._calc_formula = None

    @property
    def calc_condition(self):
        return self._calc_condition

    @calc_condition.setter
    def calc_condition(self, value):
        if isinstance(value, VcpCalcCondition):
            self._calc_condition = value
        else:
            self._calc_condition = VcpCalcCondition.from_alipay_dict(value)
    @property
    def calc_formula(self):
        return self._calc_formula

    @calc_formula.setter
    def calc_formula(self, value):
        if isinstance(value, VcpCalcFormula):
            self._calc_formula = value
        else:
            self._calc_formula = VcpCalcFormula.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.calc_condition:
            if hasattr(self.calc_condition, 'to_alipay_dict'):
                params['calc_condition'] = self.calc_condition.to_alipay_dict()
            else:
                params['calc_condition'] = self.calc_condition
        if self.calc_formula:
            if hasattr(self.calc_formula, 'to_alipay_dict'):
                params['calc_formula'] = self.calc_formula.to_alipay_dict()
            else:
                params['calc_formula'] = self.calc_formula
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VcpCalcRule()
        if 'calc_condition' in d:
            o.calc_condition = d['calc_condition']
        if 'calc_formula' in d:
            o.calc_formula = d['calc_formula']
        return o


