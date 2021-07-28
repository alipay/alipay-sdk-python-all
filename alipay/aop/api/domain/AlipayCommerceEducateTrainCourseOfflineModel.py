#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateTrainCourseOfflineModel(object):

    def __init__(self):
        self._biz_type = None
        self._course_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.course_id:
            if hasattr(self.course_id, 'to_alipay_dict'):
                params['course_id'] = self.course_id.to_alipay_dict()
            else:
                params['course_id'] = self.course_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTrainCourseOfflineModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'course_id' in d:
            o.course_id = d['course_id']
        return o


