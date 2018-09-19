#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GradeDiscountPoint(object):

    def __init__(self):
        self._benefit_id = None
        self._discount_point = None
        self._grade = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def discount_point(self):
        return self._discount_point

    @discount_point.setter
    def discount_point(self, value):
        self._discount_point = value
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.discount_point:
            if hasattr(self.discount_point, 'to_alipay_dict'):
                params['discount_point'] = self.discount_point.to_alipay_dict()
            else:
                params['discount_point'] = self.discount_point
        if self.grade:
            if hasattr(self.grade, 'to_alipay_dict'):
                params['grade'] = self.grade.to_alipay_dict()
            else:
                params['grade'] = self.grade
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GradeDiscountPoint()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'discount_point' in d:
            o.discount_point = d['discount_point']
        if 'grade' in d:
            o.grade = d['grade']
        return o


