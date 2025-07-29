#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduClassTeacher(object):

    def __init__(self):
        self._teacher_id = None
        self._teacher_name = None

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
        o = EduClassTeacher()
        if 'teacher_id' in d:
            o.teacher_id = d['teacher_id']
        if 'teacher_name' in d:
            o.teacher_name = d['teacher_name']
        return o


