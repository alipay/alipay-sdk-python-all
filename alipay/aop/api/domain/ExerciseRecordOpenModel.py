#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExerciseCourseOpenModel import ExerciseCourseOpenModel
from alipay.aop.api.domain.ExerciseDailySummaryOpenModel import ExerciseDailySummaryOpenModel
from alipay.aop.api.domain.ExerciseItemOpenModel import ExerciseItemOpenModel


class ExerciseRecordOpenModel(object):

    def __init__(self):
        self._biz_type = None
        self._course_list = None
        self._daily_summary = None
        self._item_list = None
        self._proposal_list = None
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
        if isinstance(value, ExerciseCourseOpenModel):
            self._course_list = value
        else:
            self._course_list = ExerciseCourseOpenModel.from_alipay_dict(value)
    @property
    def daily_summary(self):
        return self._daily_summary

    @daily_summary.setter
    def daily_summary(self, value):
        if isinstance(value, list):
            self._daily_summary = list()
            for i in value:
                if isinstance(i, ExerciseDailySummaryOpenModel):
                    self._daily_summary.append(i)
                else:
                    self._daily_summary.append(ExerciseDailySummaryOpenModel.from_alipay_dict(i))
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
    def proposal_list(self):
        return self._proposal_list

    @proposal_list.setter
    def proposal_list(self, value):
        if isinstance(value, list):
            self._proposal_list = list()
            for i in value:
                self._proposal_list.append(i)
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
            if hasattr(self.course_list, 'to_alipay_dict'):
                params['course_list'] = self.course_list.to_alipay_dict()
            else:
                params['course_list'] = self.course_list
        if self.daily_summary:
            if isinstance(self.daily_summary, list):
                for i in range(0, len(self.daily_summary)):
                    element = self.daily_summary[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.daily_summary[i] = element.to_alipay_dict()
            if hasattr(self.daily_summary, 'to_alipay_dict'):
                params['daily_summary'] = self.daily_summary.to_alipay_dict()
            else:
                params['daily_summary'] = self.daily_summary
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
        if self.proposal_list:
            if isinstance(self.proposal_list, list):
                for i in range(0, len(self.proposal_list)):
                    element = self.proposal_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.proposal_list[i] = element.to_alipay_dict()
            if hasattr(self.proposal_list, 'to_alipay_dict'):
                params['proposal_list'] = self.proposal_list.to_alipay_dict()
            else:
                params['proposal_list'] = self.proposal_list
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
        o = ExerciseRecordOpenModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'course_list' in d:
            o.course_list = d['course_list']
        if 'daily_summary' in d:
            o.daily_summary = d['daily_summary']
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'proposal_list' in d:
            o.proposal_list = d['proposal_list']
        if 'time_dimension_type' in d:
            o.time_dimension_type = d['time_dimension_type']
        if 'values' in d:
            o.values = d['values']
        return o


