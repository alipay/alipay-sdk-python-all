#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataItemLimitPeriodInfo(object):

    def __init__(self):
        self._rule = None
        self._unit = None
        self._value = None

    @property
    def rule(self):
        return self._rule

    @rule.setter
    def rule(self, value):
        self._rule = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, list):
            self._value = list()
            for i in value:
                self._value.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.rule:
            if hasattr(self.rule, 'to_alipay_dict'):
                params['rule'] = self.rule.to_alipay_dict()
            else:
                params['rule'] = self.rule
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        if self.value:
            if isinstance(self.value, list):
                for i in range(0, len(self.value)):
                    element = self.value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.value[i] = element.to_alipay_dict()
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataItemLimitPeriodInfo()
        if 'rule' in d:
            o.rule = d['rule']
        if 'unit' in d:
            o.unit = d['unit']
        if 'value' in d:
            o.value = d['value']
        return o


