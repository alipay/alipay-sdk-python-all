#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitEnrollRuleData import RecruitEnrollRuleData


class RecruitEnrollRule(object):

    def __init__(self):
        self._max_size = None
        self._min_size = None
        self._required = None
        self._rule_data = None
        self._type = None

    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        self._max_size = value
    @property
    def min_size(self):
        return self._min_size

    @min_size.setter
    def min_size(self, value):
        self._min_size = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def rule_data(self):
        return self._rule_data

    @rule_data.setter
    def rule_data(self, value):
        if isinstance(value, RecruitEnrollRuleData):
            self._rule_data = value
        else:
            self._rule_data = RecruitEnrollRuleData.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_size:
            if hasattr(self.max_size, 'to_alipay_dict'):
                params['max_size'] = self.max_size.to_alipay_dict()
            else:
                params['max_size'] = self.max_size
        if self.min_size:
            if hasattr(self.min_size, 'to_alipay_dict'):
                params['min_size'] = self.min_size.to_alipay_dict()
            else:
                params['min_size'] = self.min_size
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        if self.rule_data:
            if hasattr(self.rule_data, 'to_alipay_dict'):
                params['rule_data'] = self.rule_data.to_alipay_dict()
            else:
                params['rule_data'] = self.rule_data
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitEnrollRule()
        if 'max_size' in d:
            o.max_size = d['max_size']
        if 'min_size' in d:
            o.min_size = d['min_size']
        if 'required' in d:
            o.required = d['required']
        if 'rule_data' in d:
            o.rule_data = d['rule_data']
        if 'type' in d:
            o.type = d['type']
        return o


