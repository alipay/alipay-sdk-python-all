#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsLessonUserlessonrecordSyncModel(object):

    def __init__(self):
        self._data_source = None
        self._lesson_out_id = None
        self._open_id = None
        self._out_biz_id = None
        self._record_time = None
        self._study_calorie = None
        self._study_duration = None
        self._user_id = None

    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def lesson_out_id(self):
        return self._lesson_out_id

    @lesson_out_id.setter
    def lesson_out_id(self, value):
        self._lesson_out_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def record_time(self):
        return self._record_time

    @record_time.setter
    def record_time(self, value):
        self._record_time = value
    @property
    def study_calorie(self):
        return self._study_calorie

    @study_calorie.setter
    def study_calorie(self, value):
        self._study_calorie = value
    @property
    def study_duration(self):
        return self._study_duration

    @study_duration.setter
    def study_duration(self, value):
        self._study_duration = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.lesson_out_id:
            if hasattr(self.lesson_out_id, 'to_alipay_dict'):
                params['lesson_out_id'] = self.lesson_out_id.to_alipay_dict()
            else:
                params['lesson_out_id'] = self.lesson_out_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.record_time:
            if hasattr(self.record_time, 'to_alipay_dict'):
                params['record_time'] = self.record_time.to_alipay_dict()
            else:
                params['record_time'] = self.record_time
        if self.study_calorie:
            if hasattr(self.study_calorie, 'to_alipay_dict'):
                params['study_calorie'] = self.study_calorie.to_alipay_dict()
            else:
                params['study_calorie'] = self.study_calorie
        if self.study_duration:
            if hasattr(self.study_duration, 'to_alipay_dict'):
                params['study_duration'] = self.study_duration.to_alipay_dict()
            else:
                params['study_duration'] = self.study_duration
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsLessonUserlessonrecordSyncModel()
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'lesson_out_id' in d:
            o.lesson_out_id = d['lesson_out_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'record_time' in d:
            o.record_time = d['record_time']
        if 'study_calorie' in d:
            o.study_calorie = d['study_calorie']
        if 'study_duration' in d:
            o.study_duration = d['study_duration']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


