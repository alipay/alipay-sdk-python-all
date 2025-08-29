#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TeacherVO(object):

    def __init__(self):
        self._teacher_introduce = None
        self._teacher_name = None
        self._teacher_picture = None

    @property
    def teacher_introduce(self):
        return self._teacher_introduce

    @teacher_introduce.setter
    def teacher_introduce(self, value):
        self._teacher_introduce = value
    @property
    def teacher_name(self):
        return self._teacher_name

    @teacher_name.setter
    def teacher_name(self, value):
        self._teacher_name = value
    @property
    def teacher_picture(self):
        return self._teacher_picture

    @teacher_picture.setter
    def teacher_picture(self, value):
        self._teacher_picture = value


    def to_alipay_dict(self):
        params = dict()
        if self.teacher_introduce:
            if hasattr(self.teacher_introduce, 'to_alipay_dict'):
                params['teacher_introduce'] = self.teacher_introduce.to_alipay_dict()
            else:
                params['teacher_introduce'] = self.teacher_introduce
        if self.teacher_name:
            if hasattr(self.teacher_name, 'to_alipay_dict'):
                params['teacher_name'] = self.teacher_name.to_alipay_dict()
            else:
                params['teacher_name'] = self.teacher_name
        if self.teacher_picture:
            if hasattr(self.teacher_picture, 'to_alipay_dict'):
                params['teacher_picture'] = self.teacher_picture.to_alipay_dict()
            else:
                params['teacher_picture'] = self.teacher_picture
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TeacherVO()
        if 'teacher_introduce' in d:
            o.teacher_introduce = d['teacher_introduce']
        if 'teacher_name' in d:
            o.teacher_name = d['teacher_name']
        if 'teacher_picture' in d:
            o.teacher_picture = d['teacher_picture']
        return o


