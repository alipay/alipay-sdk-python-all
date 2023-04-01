#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JobWorthCourseTeacher(object):

    def __init__(self):
        self._desc = None
        self._id_type = None
        self._teacher_id = None
        self._teacher_name = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        self._teacher_id = value
    @property
    def teacher_name(self):
        return self._teacher_name

    @teacher_name.setter
    def teacher_name(self, value):
        self._teacher_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.teacher_id:
            if hasattr(self.teacher_id, 'to_alipay_dict'):
                params['teacher_id'] = self.teacher_id.to_alipay_dict()
            else:
                params['teacher_id'] = self.teacher_id
        if self.teacher_name:
            if hasattr(self.teacher_name, 'to_alipay_dict'):
                params['teacher_name'] = self.teacher_name.to_alipay_dict()
            else:
                params['teacher_name'] = self.teacher_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JobWorthCourseTeacher()
        if 'desc' in d:
            o.desc = d['desc']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'teacher_id' in d:
            o.teacher_id = d['teacher_id']
        if 'teacher_name' in d:
            o.teacher_name = d['teacher_name']
        return o


