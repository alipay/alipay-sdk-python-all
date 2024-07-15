#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalShopMarketingActivityRule import MedicalShopMarketingActivityRule


class MedicalShopMarketingActivity(object):

    def __init__(self):
        self._activity_rule = None
        self._activity_type = None
        self._end_time = None
        self._start_time = None

    @property
    def activity_rule(self):
        return self._activity_rule

    @activity_rule.setter
    def activity_rule(self, value):
        if isinstance(value, list):
            self._activity_rule = list()
            for i in value:
                if isinstance(i, MedicalShopMarketingActivityRule):
                    self._activity_rule.append(i)
                else:
                    self._activity_rule.append(MedicalShopMarketingActivityRule.from_alipay_dict(i))
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_rule:
            if isinstance(self.activity_rule, list):
                for i in range(0, len(self.activity_rule)):
                    element = self.activity_rule[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_rule[i] = element.to_alipay_dict()
            if hasattr(self.activity_rule, 'to_alipay_dict'):
                params['activity_rule'] = self.activity_rule.to_alipay_dict()
            else:
                params['activity_rule'] = self.activity_rule
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalShopMarketingActivity()
        if 'activity_rule' in d:
            o.activity_rule = d['activity_rule']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


