#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClassRateInfo(object):

    def __init__(self):
        self._grade = None
        self._grade_desc = None
        self._rate = None
        self._rate_amount = None

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value
    @property
    def grade_desc(self):
        return self._grade_desc

    @grade_desc.setter
    def grade_desc(self, value):
        self._grade_desc = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def rate_amount(self):
        return self._rate_amount

    @rate_amount.setter
    def rate_amount(self, value):
        self._rate_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.grade:
            if hasattr(self.grade, 'to_alipay_dict'):
                params['grade'] = self.grade.to_alipay_dict()
            else:
                params['grade'] = self.grade
        if self.grade_desc:
            if hasattr(self.grade_desc, 'to_alipay_dict'):
                params['grade_desc'] = self.grade_desc.to_alipay_dict()
            else:
                params['grade_desc'] = self.grade_desc
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.rate_amount:
            if hasattr(self.rate_amount, 'to_alipay_dict'):
                params['rate_amount'] = self.rate_amount.to_alipay_dict()
            else:
                params['rate_amount'] = self.rate_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClassRateInfo()
        if 'grade' in d:
            o.grade = d['grade']
        if 'grade_desc' in d:
            o.grade_desc = d['grade_desc']
        if 'rate' in d:
            o.rate = d['rate']
        if 'rate_amount' in d:
            o.rate_amount = d['rate_amount']
        return o


