#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCareertrainingCourseQueryModel(object):

    def __init__(self):
        self._course_id = None
        self._need_edit_version = None
        self._out_course_id = None

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def need_edit_version(self):
        return self._need_edit_version

    @need_edit_version.setter
    def need_edit_version(self, value):
        self._need_edit_version = value
    @property
    def out_course_id(self):
        return self._out_course_id

    @out_course_id.setter
    def out_course_id(self, value):
        self._out_course_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.course_id:
            if hasattr(self.course_id, 'to_alipay_dict'):
                params['course_id'] = self.course_id.to_alipay_dict()
            else:
                params['course_id'] = self.course_id
        if self.need_edit_version:
            if hasattr(self.need_edit_version, 'to_alipay_dict'):
                params['need_edit_version'] = self.need_edit_version.to_alipay_dict()
            else:
                params['need_edit_version'] = self.need_edit_version
        if self.out_course_id:
            if hasattr(self.out_course_id, 'to_alipay_dict'):
                params['out_course_id'] = self.out_course_id.to_alipay_dict()
            else:
                params['out_course_id'] = self.out_course_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCareertrainingCourseQueryModel()
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'need_edit_version' in d:
            o.need_edit_version = d['need_edit_version']
        if 'out_course_id' in d:
            o.out_course_id = d['out_course_id']
        return o


