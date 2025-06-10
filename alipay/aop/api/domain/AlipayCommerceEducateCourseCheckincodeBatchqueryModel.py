#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCourseCheckincodeBatchqueryModel(object):

    def __init__(self):
        self._course_rule_id = None
        self._course_rule_name = None
        self._enable_status = None
        self._inst_id = None
        self._page_num = None
        self._page_size = None
        self._roster_id = None

    @property
    def course_rule_id(self):
        return self._course_rule_id

    @course_rule_id.setter
    def course_rule_id(self, value):
        self._course_rule_id = value
    @property
    def course_rule_name(self):
        return self._course_rule_name

    @course_rule_name.setter
    def course_rule_name(self, value):
        self._course_rule_name = value
    @property
    def enable_status(self):
        return self._enable_status

    @enable_status.setter
    def enable_status(self, value):
        self._enable_status = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
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
        if self.course_rule_name:
            if hasattr(self.course_rule_name, 'to_alipay_dict'):
                params['course_rule_name'] = self.course_rule_name.to_alipay_dict()
            else:
                params['course_rule_name'] = self.course_rule_name
        if self.enable_status:
            if hasattr(self.enable_status, 'to_alipay_dict'):
                params['enable_status'] = self.enable_status.to_alipay_dict()
            else:
                params['enable_status'] = self.enable_status
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
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
        o = AlipayCommerceEducateCourseCheckincodeBatchqueryModel()
        if 'course_rule_id' in d:
            o.course_rule_id = d['course_rule_id']
        if 'course_rule_name' in d:
            o.course_rule_name = d['course_rule_name']
        if 'enable_status' in d:
            o.enable_status = d['enable_status']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'roster_id' in d:
            o.roster_id = d['roster_id']
        return o


