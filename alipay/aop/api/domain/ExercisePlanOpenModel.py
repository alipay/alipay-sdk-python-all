#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExerciseCourseOpenModel import ExerciseCourseOpenModel
from alipay.aop.api.domain.ExerciseItemOpenModel import ExerciseItemOpenModel


class ExercisePlanOpenModel(object):

    def __init__(self):
        self._biz_type = None
        self._course_list = None
        self._item_list = None
        self._time_dimension_type = None
        self._values = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def course_list(self):
        return self._course_list

    @course_list.setter
    def course_list(self, value):
        if isinstance(value, list):
            self._course_list = list()
            for i in value:
                if isinstance(i, ExerciseCourseOpenModel):
                    self._course_list.append(i)
                else:
                    self._course_list.append(ExerciseCourseOpenModel.from_alipay_dict(i))
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, ExerciseItemOpenModel):
                    self._item_list.append(i)
                else:
                    self._item_list.append(ExerciseItemOpenModel.from_alipay_dict(i))
    @property
    def time_dimension_type(self):
        return self._time_dimension_type

    @time_dimension_type.setter
    def time_dimension_type(self, value):
        self._time_dimension_type = value
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        self._values = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.course_list:
            if isinstance(self.course_list, list):
                for i in range(0, len(self.course_list)):
                    element = self.course_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.course_list[i] = element.to_alipay_dict()
            if hasattr(self.course_list, 'to_alipay_dict'):
                params['course_list'] = self.course_list.to_alipay_dict()
            else:
                params['course_list'] = self.course_list
        if self.item_list:
            if isinstance(self.item_list, list):
                for i in range(0, len(self.item_list)):
                    element = self.item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_list[i] = element.to_alipay_dict()
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
        if self.time_dimension_type:
            if hasattr(self.time_dimension_type, 'to_alipay_dict'):
                params['time_dimension_type'] = self.time_dimension_type.to_alipay_dict()
            else:
                params['time_dimension_type'] = self.time_dimension_type
        if self.values:
            if hasattr(self.values, 'to_alipay_dict'):
                params['values'] = self.values.to_alipay_dict()
            else:
                params['values'] = self.values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExercisePlanOpenModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'course_list' in d:
            o.course_list = d['course_list']
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'time_dimension_type' in d:
            o.time_dimension_type = d['time_dimension_type']
        if 'values' in d:
            o.values = d['values']
        return o


