#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TimePeriodRule(object):

    def __init__(self):
        self._end_time = None
        self._rule_info = None
        self._rule_type = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def rule_info(self):
        return self._rule_info

    @rule_info.setter
    def rule_info(self, value):
        if isinstance(value, list):
            self._rule_info = list()
            for i in value:
                self._rule_info.append(i)
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.rule_info:
            if isinstance(self.rule_info, list):
                for i in range(0, len(self.rule_info)):
                    element = self.rule_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rule_info[i] = element.to_alipay_dict()
            if hasattr(self.rule_info, 'to_alipay_dict'):
                params['rule_info'] = self.rule_info.to_alipay_dict()
            else:
                params['rule_info'] = self.rule_info
        if self.rule_type:
            if hasattr(self.rule_type, 'to_alipay_dict'):
                params['rule_type'] = self.rule_type.to_alipay_dict()
            else:
                params['rule_type'] = self.rule_type
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
        o = TimePeriodRule()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'rule_info' in d:
            o.rule_info = d['rule_info']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


