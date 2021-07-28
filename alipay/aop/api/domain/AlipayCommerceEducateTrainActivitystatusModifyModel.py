#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateTrainActivitystatusModifyModel(object):

    def __init__(self):
        self._activity_id = None
        self._apply_status = None
        self._course_id = None
        self._encode_mobile = None
        self._fail_desc = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def encode_mobile(self):
        return self._encode_mobile

    @encode_mobile.setter
    def encode_mobile(self, value):
        self._encode_mobile = value
    @property
    def fail_desc(self):
        return self._fail_desc

    @fail_desc.setter
    def fail_desc(self, value):
        self._fail_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.course_id:
            if hasattr(self.course_id, 'to_alipay_dict'):
                params['course_id'] = self.course_id.to_alipay_dict()
            else:
                params['course_id'] = self.course_id
        if self.encode_mobile:
            if hasattr(self.encode_mobile, 'to_alipay_dict'):
                params['encode_mobile'] = self.encode_mobile.to_alipay_dict()
            else:
                params['encode_mobile'] = self.encode_mobile
        if self.fail_desc:
            if hasattr(self.fail_desc, 'to_alipay_dict'):
                params['fail_desc'] = self.fail_desc.to_alipay_dict()
            else:
                params['fail_desc'] = self.fail_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTrainActivitystatusModifyModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'encode_mobile' in d:
            o.encode_mobile = d['encode_mobile']
        if 'fail_desc' in d:
            o.fail_desc = d['fail_desc']
        return o


