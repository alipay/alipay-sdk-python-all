#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceFhyeduLearnplanSyncModel(object):

    def __init__(self):
        self._assign_time = None
        self._content = None
        self._dead_line_time = None
        self._homework_id = None
        self._inst_id = None
        self._student_id = None

    @property
    def assign_time(self):
        return self._assign_time

    @assign_time.setter
    def assign_time(self, value):
        self._assign_time = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def dead_line_time(self):
        return self._dead_line_time

    @dead_line_time.setter
    def dead_line_time(self, value):
        self._dead_line_time = value
    @property
    def homework_id(self):
        return self._homework_id

    @homework_id.setter
    def homework_id(self, value):
        self._homework_id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.assign_time:
            if hasattr(self.assign_time, 'to_alipay_dict'):
                params['assign_time'] = self.assign_time.to_alipay_dict()
            else:
                params['assign_time'] = self.assign_time
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.dead_line_time:
            if hasattr(self.dead_line_time, 'to_alipay_dict'):
                params['dead_line_time'] = self.dead_line_time.to_alipay_dict()
            else:
                params['dead_line_time'] = self.dead_line_time
        if self.homework_id:
            if hasattr(self.homework_id, 'to_alipay_dict'):
                params['homework_id'] = self.homework_id.to_alipay_dict()
            else:
                params['homework_id'] = self.homework_id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.student_id:
            if hasattr(self.student_id, 'to_alipay_dict'):
                params['student_id'] = self.student_id.to_alipay_dict()
            else:
                params['student_id'] = self.student_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceFhyeduLearnplanSyncModel()
        if 'assign_time' in d:
            o.assign_time = d['assign_time']
        if 'content' in d:
            o.content = d['content']
        if 'dead_line_time' in d:
            o.dead_line_time = d['dead_line_time']
        if 'homework_id' in d:
            o.homework_id = d['homework_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'student_id' in d:
            o.student_id = d['student_id']
        return o


