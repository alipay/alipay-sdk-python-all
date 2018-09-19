#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GradeDiscountPoint import GradeDiscountPoint


class BenefitGradePoint(object):

    def __init__(self):
        self._benefit_id = None
        self._grade_points = None
        self._original_point = None
        self._own_grades = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def grade_points(self):
        return self._grade_points

    @grade_points.setter
    def grade_points(self, value):
        if isinstance(value, list):
            self._grade_points = list()
            for i in value:
                if isinstance(i, GradeDiscountPoint):
                    self._grade_points.append(i)
                else:
                    self._grade_points.append(GradeDiscountPoint.from_alipay_dict(i))
    @property
    def original_point(self):
        return self._original_point

    @original_point.setter
    def original_point(self, value):
        self._original_point = value
    @property
    def own_grades(self):
        return self._own_grades

    @own_grades.setter
    def own_grades(self, value):
        self._own_grades = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.grade_points:
            if isinstance(self.grade_points, list):
                for i in range(0, len(self.grade_points)):
                    element = self.grade_points[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.grade_points[i] = element.to_alipay_dict()
            if hasattr(self.grade_points, 'to_alipay_dict'):
                params['grade_points'] = self.grade_points.to_alipay_dict()
            else:
                params['grade_points'] = self.grade_points
        if self.original_point:
            if hasattr(self.original_point, 'to_alipay_dict'):
                params['original_point'] = self.original_point.to_alipay_dict()
            else:
                params['original_point'] = self.original_point
        if self.own_grades:
            if hasattr(self.own_grades, 'to_alipay_dict'):
                params['own_grades'] = self.own_grades.to_alipay_dict()
            else:
                params['own_grades'] = self.own_grades
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitGradePoint()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'grade_points' in d:
            o.grade_points = d['grade_points']
        if 'original_point' in d:
            o.original_point = d['original_point']
        if 'own_grades' in d:
            o.own_grades = d['own_grades']
        return o


