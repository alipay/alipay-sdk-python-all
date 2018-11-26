#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NoticeTemplateArgs(object):

    def __init__(self):
        self._course_start_time = None

    @property
    def course_start_time(self):
        return self._course_start_time

    @course_start_time.setter
    def course_start_time(self, value):
        self._course_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.course_start_time:
            if hasattr(self.course_start_time, 'to_alipay_dict'):
                params['course_start_time'] = self.course_start_time.to_alipay_dict()
            else:
                params['course_start_time'] = self.course_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NoticeTemplateArgs()
        if 'course_start_time' in d:
            o.course_start_time = d['course_start_time']
        return o


