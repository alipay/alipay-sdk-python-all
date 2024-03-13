#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EvaluateIndicateGrade(object):

    def __init__(self):
        self._grade_unit = None
        self._grade_value = None
        self._perfect_value = None

    @property
    def grade_unit(self):
        return self._grade_unit

    @grade_unit.setter
    def grade_unit(self, value):
        self._grade_unit = value
    @property
    def grade_value(self):
        return self._grade_value

    @grade_value.setter
    def grade_value(self, value):
        self._grade_value = value
    @property
    def perfect_value(self):
        return self._perfect_value

    @perfect_value.setter
    def perfect_value(self, value):
        self._perfect_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.grade_unit:
            if hasattr(self.grade_unit, 'to_alipay_dict'):
                params['grade_unit'] = self.grade_unit.to_alipay_dict()
            else:
                params['grade_unit'] = self.grade_unit
        if self.grade_value:
            if hasattr(self.grade_value, 'to_alipay_dict'):
                params['grade_value'] = self.grade_value.to_alipay_dict()
            else:
                params['grade_value'] = self.grade_value
        if self.perfect_value:
            if hasattr(self.perfect_value, 'to_alipay_dict'):
                params['perfect_value'] = self.perfect_value.to_alipay_dict()
            else:
                params['perfect_value'] = self.perfect_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EvaluateIndicateGrade()
        if 'grade_unit' in d:
            o.grade_unit = d['grade_unit']
        if 'grade_value' in d:
            o.grade_value = d['grade_value']
        if 'perfect_value' in d:
            o.perfect_value = d['perfect_value']
        return o


