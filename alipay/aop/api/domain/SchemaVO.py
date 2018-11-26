#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoanTerm import LoanTerm


class SchemaVO(object):

    def __init__(self):
        self._daily_risk_int_rate = None
        self._max_apply_amt = None
        self._min_apply_amt = None
        self._repay_mode_list = None
        self._term_list = None

    @property
    def daily_risk_int_rate(self):
        return self._daily_risk_int_rate

    @daily_risk_int_rate.setter
    def daily_risk_int_rate(self, value):
        self._daily_risk_int_rate = value
    @property
    def max_apply_amt(self):
        return self._max_apply_amt

    @max_apply_amt.setter
    def max_apply_amt(self, value):
        self._max_apply_amt = value
    @property
    def min_apply_amt(self):
        return self._min_apply_amt

    @min_apply_amt.setter
    def min_apply_amt(self, value):
        self._min_apply_amt = value
    @property
    def repay_mode_list(self):
        return self._repay_mode_list

    @repay_mode_list.setter
    def repay_mode_list(self, value):
        if isinstance(value, list):
            self._repay_mode_list = list()
            for i in value:
                self._repay_mode_list.append(i)
    @property
    def term_list(self):
        return self._term_list

    @term_list.setter
    def term_list(self, value):
        if isinstance(value, list):
            self._term_list = list()
            for i in value:
                if isinstance(i, LoanTerm):
                    self._term_list.append(i)
                else:
                    self._term_list.append(LoanTerm.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.daily_risk_int_rate:
            if hasattr(self.daily_risk_int_rate, 'to_alipay_dict'):
                params['daily_risk_int_rate'] = self.daily_risk_int_rate.to_alipay_dict()
            else:
                params['daily_risk_int_rate'] = self.daily_risk_int_rate
        if self.max_apply_amt:
            if hasattr(self.max_apply_amt, 'to_alipay_dict'):
                params['max_apply_amt'] = self.max_apply_amt.to_alipay_dict()
            else:
                params['max_apply_amt'] = self.max_apply_amt
        if self.min_apply_amt:
            if hasattr(self.min_apply_amt, 'to_alipay_dict'):
                params['min_apply_amt'] = self.min_apply_amt.to_alipay_dict()
            else:
                params['min_apply_amt'] = self.min_apply_amt
        if self.repay_mode_list:
            if isinstance(self.repay_mode_list, list):
                for i in range(0, len(self.repay_mode_list)):
                    element = self.repay_mode_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repay_mode_list[i] = element.to_alipay_dict()
            if hasattr(self.repay_mode_list, 'to_alipay_dict'):
                params['repay_mode_list'] = self.repay_mode_list.to_alipay_dict()
            else:
                params['repay_mode_list'] = self.repay_mode_list
        if self.term_list:
            if isinstance(self.term_list, list):
                for i in range(0, len(self.term_list)):
                    element = self.term_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.term_list[i] = element.to_alipay_dict()
            if hasattr(self.term_list, 'to_alipay_dict'):
                params['term_list'] = self.term_list.to_alipay_dict()
            else:
                params['term_list'] = self.term_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SchemaVO()
        if 'daily_risk_int_rate' in d:
            o.daily_risk_int_rate = d['daily_risk_int_rate']
        if 'max_apply_amt' in d:
            o.max_apply_amt = d['max_apply_amt']
        if 'min_apply_amt' in d:
            o.min_apply_amt = d['min_apply_amt']
        if 'repay_mode_list' in d:
            o.repay_mode_list = d['repay_mode_list']
        if 'term_list' in d:
            o.term_list = d['term_list']
        return o


