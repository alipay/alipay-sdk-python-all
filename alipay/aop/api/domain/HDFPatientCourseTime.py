#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFPatientCourseTime(object):

    def __init__(self):
        self._patient_course_time = None

    @property
    def patient_course_time(self):
        return self._patient_course_time

    @patient_course_time.setter
    def patient_course_time(self, value):
        self._patient_course_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.patient_course_time:
            if hasattr(self.patient_course_time, 'to_alipay_dict'):
                params['patient_course_time'] = self.patient_course_time.to_alipay_dict()
            else:
                params['patient_course_time'] = self.patient_course_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFPatientCourseTime()
        if 'patient_course_time' in d:
            o.patient_course_time = d['patient_course_time']
        return o


