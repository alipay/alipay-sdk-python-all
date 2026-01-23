#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCareertrainingCoursePublishModel(object):

    def __init__(self):
        self._course_id = None
        self._publish_status = None

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def publish_status(self):
        return self._publish_status

    @publish_status.setter
    def publish_status(self, value):
        self._publish_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.course_id:
            if hasattr(self.course_id, 'to_alipay_dict'):
                params['course_id'] = self.course_id.to_alipay_dict()
            else:
                params['course_id'] = self.course_id
        if self.publish_status:
            if hasattr(self.publish_status, 'to_alipay_dict'):
                params['publish_status'] = self.publish_status.to_alipay_dict()
            else:
                params['publish_status'] = self.publish_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCareertrainingCoursePublishModel()
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'publish_status' in d:
            o.publish_status = d['publish_status']
        return o


