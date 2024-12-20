#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PenaltyAmount import PenaltyAmount
from alipay.aop.api.domain.PenaltyPercent import PenaltyPercent


class CancelRule(object):

    def __init__(self):
        self._penalty_amounts = None
        self._penalty_percent = None
        self._penalty_type = None
        self._rule_end_time = None
        self._rule_start_time = None

    @property
    def penalty_amounts(self):
        return self._penalty_amounts

    @penalty_amounts.setter
    def penalty_amounts(self, value):
        if isinstance(value, list):
            self._penalty_amounts = list()
            for i in value:
                if isinstance(i, PenaltyAmount):
                    self._penalty_amounts.append(i)
                else:
                    self._penalty_amounts.append(PenaltyAmount.from_alipay_dict(i))
    @property
    def penalty_percent(self):
        return self._penalty_percent

    @penalty_percent.setter
    def penalty_percent(self, value):
        if isinstance(value, PenaltyPercent):
            self._penalty_percent = value
        else:
            self._penalty_percent = PenaltyPercent.from_alipay_dict(value)
    @property
    def penalty_type(self):
        return self._penalty_type

    @penalty_type.setter
    def penalty_type(self, value):
        self._penalty_type = value
    @property
    def rule_end_time(self):
        return self._rule_end_time

    @rule_end_time.setter
    def rule_end_time(self, value):
        self._rule_end_time = value
    @property
    def rule_start_time(self):
        return self._rule_start_time

    @rule_start_time.setter
    def rule_start_time(self, value):
        self._rule_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.penalty_amounts:
            if isinstance(self.penalty_amounts, list):
                for i in range(0, len(self.penalty_amounts)):
                    element = self.penalty_amounts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.penalty_amounts[i] = element.to_alipay_dict()
            if hasattr(self.penalty_amounts, 'to_alipay_dict'):
                params['penalty_amounts'] = self.penalty_amounts.to_alipay_dict()
            else:
                params['penalty_amounts'] = self.penalty_amounts
        if self.penalty_percent:
            if hasattr(self.penalty_percent, 'to_alipay_dict'):
                params['penalty_percent'] = self.penalty_percent.to_alipay_dict()
            else:
                params['penalty_percent'] = self.penalty_percent
        if self.penalty_type:
            if hasattr(self.penalty_type, 'to_alipay_dict'):
                params['penalty_type'] = self.penalty_type.to_alipay_dict()
            else:
                params['penalty_type'] = self.penalty_type
        if self.rule_end_time:
            if hasattr(self.rule_end_time, 'to_alipay_dict'):
                params['rule_end_time'] = self.rule_end_time.to_alipay_dict()
            else:
                params['rule_end_time'] = self.rule_end_time
        if self.rule_start_time:
            if hasattr(self.rule_start_time, 'to_alipay_dict'):
                params['rule_start_time'] = self.rule_start_time.to_alipay_dict()
            else:
                params['rule_start_time'] = self.rule_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CancelRule()
        if 'penalty_amounts' in d:
            o.penalty_amounts = d['penalty_amounts']
        if 'penalty_percent' in d:
            o.penalty_percent = d['penalty_percent']
        if 'penalty_type' in d:
            o.penalty_type = d['penalty_type']
        if 'rule_end_time' in d:
            o.rule_end_time = d['rule_end_time']
        if 'rule_start_time' in d:
            o.rule_start_time = d['rule_start_time']
        return o


