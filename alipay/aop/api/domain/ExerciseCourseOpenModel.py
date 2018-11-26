#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExerciseCourseOpenModel(object):

    def __init__(self):
        self._biz_type = None
        self._classroom = None
        self._course_detail_url = None
        self._craftsman_id = None
        self._craftsman_name = None
        self._craftsman_title = None
        self._end_time = None
        self._external_course_id = None
        self._name = None
        self._source_type = None
        self._start_time = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def classroom(self):
        return self._classroom

    @classroom.setter
    def classroom(self, value):
        self._classroom = value
    @property
    def course_detail_url(self):
        return self._course_detail_url

    @course_detail_url.setter
    def course_detail_url(self, value):
        self._course_detail_url = value
    @property
    def craftsman_id(self):
        return self._craftsman_id

    @craftsman_id.setter
    def craftsman_id(self, value):
        self._craftsman_id = value
    @property
    def craftsman_name(self):
        return self._craftsman_name

    @craftsman_name.setter
    def craftsman_name(self, value):
        self._craftsman_name = value
    @property
    def craftsman_title(self):
        return self._craftsman_title

    @craftsman_title.setter
    def craftsman_title(self, value):
        self._craftsman_title = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def external_course_id(self):
        return self._external_course_id

    @external_course_id.setter
    def external_course_id(self, value):
        self._external_course_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.classroom:
            if hasattr(self.classroom, 'to_alipay_dict'):
                params['classroom'] = self.classroom.to_alipay_dict()
            else:
                params['classroom'] = self.classroom
        if self.course_detail_url:
            if hasattr(self.course_detail_url, 'to_alipay_dict'):
                params['course_detail_url'] = self.course_detail_url.to_alipay_dict()
            else:
                params['course_detail_url'] = self.course_detail_url
        if self.craftsman_id:
            if hasattr(self.craftsman_id, 'to_alipay_dict'):
                params['craftsman_id'] = self.craftsman_id.to_alipay_dict()
            else:
                params['craftsman_id'] = self.craftsman_id
        if self.craftsman_name:
            if hasattr(self.craftsman_name, 'to_alipay_dict'):
                params['craftsman_name'] = self.craftsman_name.to_alipay_dict()
            else:
                params['craftsman_name'] = self.craftsman_name
        if self.craftsman_title:
            if hasattr(self.craftsman_title, 'to_alipay_dict'):
                params['craftsman_title'] = self.craftsman_title.to_alipay_dict()
            else:
                params['craftsman_title'] = self.craftsman_title
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.external_course_id:
            if hasattr(self.external_course_id, 'to_alipay_dict'):
                params['external_course_id'] = self.external_course_id.to_alipay_dict()
            else:
                params['external_course_id'] = self.external_course_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
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
        o = ExerciseCourseOpenModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'classroom' in d:
            o.classroom = d['classroom']
        if 'course_detail_url' in d:
            o.course_detail_url = d['course_detail_url']
        if 'craftsman_id' in d:
            o.craftsman_id = d['craftsman_id']
        if 'craftsman_name' in d:
            o.craftsman_name = d['craftsman_name']
        if 'craftsman_title' in d:
            o.craftsman_title = d['craftsman_title']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'external_course_id' in d:
            o.external_course_id = d['external_course_id']
        if 'name' in d:
            o.name = d['name']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


