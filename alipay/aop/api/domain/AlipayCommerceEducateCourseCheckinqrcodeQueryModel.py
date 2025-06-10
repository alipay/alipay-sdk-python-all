#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCourseCheckinqrcodeQueryModel(object):

    def __init__(self):
        self._course_rule_id = None
        self._inst_id = None
        self._roster_id = None

    @property
    def course_rule_id(self):
        return self._course_rule_id

    @course_rule_id.setter
    def course_rule_id(self, value):
        self._course_rule_id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def roster_id(self):
        return self._roster_id

    @roster_id.setter
    def roster_id(self, value):
        self._roster_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.course_rule_id:
            if hasattr(self.course_rule_id, 'to_alipay_dict'):
                params['course_rule_id'] = self.course_rule_id.to_alipay_dict()
            else:
                params['course_rule_id'] = self.course_rule_id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.roster_id:
            if hasattr(self.roster_id, 'to_alipay_dict'):
                params['roster_id'] = self.roster_id.to_alipay_dict()
            else:
                params['roster_id'] = self.roster_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateCourseCheckinqrcodeQueryModel()
        if 'course_rule_id' in d:
            o.course_rule_id = d['course_rule_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'roster_id' in d:
            o.roster_id = d['roster_id']
        return o


