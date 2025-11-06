#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmCarOwnerEvaluateInfo(object):

    def __init__(self):
        self._investment_rate = None
        self._on_time_rate = None
        self._positive_feedback_rate = None

    @property
    def investment_rate(self):
        return self._investment_rate

    @investment_rate.setter
    def investment_rate(self, value):
        self._investment_rate = value
    @property
    def on_time_rate(self):
        return self._on_time_rate

    @on_time_rate.setter
    def on_time_rate(self, value):
        self._on_time_rate = value
    @property
    def positive_feedback_rate(self):
        return self._positive_feedback_rate

    @positive_feedback_rate.setter
    def positive_feedback_rate(self, value):
        self._positive_feedback_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.investment_rate:
            if hasattr(self.investment_rate, 'to_alipay_dict'):
                params['investment_rate'] = self.investment_rate.to_alipay_dict()
            else:
                params['investment_rate'] = self.investment_rate
        if self.on_time_rate:
            if hasattr(self.on_time_rate, 'to_alipay_dict'):
                params['on_time_rate'] = self.on_time_rate.to_alipay_dict()
            else:
                params['on_time_rate'] = self.on_time_rate
        if self.positive_feedback_rate:
            if hasattr(self.positive_feedback_rate, 'to_alipay_dict'):
                params['positive_feedback_rate'] = self.positive_feedback_rate.to_alipay_dict()
            else:
                params['positive_feedback_rate'] = self.positive_feedback_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmCarOwnerEvaluateInfo()
        if 'investment_rate' in d:
            o.investment_rate = d['investment_rate']
        if 'on_time_rate' in d:
            o.on_time_rate = d['on_time_rate']
        if 'positive_feedback_rate' in d:
            o.positive_feedback_rate = d['positive_feedback_rate']
        return o


