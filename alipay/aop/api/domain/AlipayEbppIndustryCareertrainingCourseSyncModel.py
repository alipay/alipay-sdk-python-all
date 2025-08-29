#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCareertrainingCourseSyncModel(object):

    def __init__(self):
        self._course_id = None
        self._course_status = None

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def course_status(self):
        return self._course_status

    @course_status.setter
    def course_status(self, value):
        self._course_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.course_id:
            if hasattr(self.course_id, 'to_alipay_dict'):
                params['course_id'] = self.course_id.to_alipay_dict()
            else:
                params['course_id'] = self.course_id
        if self.course_status:
            if hasattr(self.course_status, 'to_alipay_dict'):
                params['course_status'] = self.course_status.to_alipay_dict()
            else:
                params['course_status'] = self.course_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCareertrainingCourseSyncModel()
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'course_status' in d:
            o.course_status = d['course_status']
        return o


