#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCourseCheckincodeCreateModel(object):

    def __init__(self):
        self._automatic_refresh = None
        self._course_id = None
        self._course_rule_id = None
        self._course_rule_name = None
        self._enable_course_rule = None
        self._end_check_in = None
        self._inst_id = None
        self._manual_close = None
        self._refresh_qr_code_frequency = None
        self._roster_id = None
        self._rule_id = None
        self._status = None

    @property
    def automatic_refresh(self):
        return self._automatic_refresh

    @automatic_refresh.setter
    def automatic_refresh(self, value):
        self._automatic_refresh = value
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
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
    def enable_course_rule(self):
        return self._enable_course_rule

    @enable_course_rule.setter
    def enable_course_rule(self, value):
        self._enable_course_rule = value
    @property
    def end_check_in(self):
        return self._end_check_in

    @end_check_in.setter
    def end_check_in(self, value):
        self._end_check_in = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def manual_close(self):
        return self._manual_close

    @manual_close.setter
    def manual_close(self, value):
        self._manual_close = value
    @property
    def refresh_qr_code_frequency(self):
        return self._refresh_qr_code_frequency

    @refresh_qr_code_frequency.setter
    def refresh_qr_code_frequency(self, value):
        self._refresh_qr_code_frequency = value
    @property
    def roster_id(self):
        return self._roster_id

    @roster_id.setter
    def roster_id(self, value):
        self._roster_id = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.automatic_refresh:
            if hasattr(self.automatic_refresh, 'to_alipay_dict'):
                params['automatic_refresh'] = self.automatic_refresh.to_alipay_dict()
            else:
                params['automatic_refresh'] = self.automatic_refresh
        if self.course_id:
            if hasattr(self.course_id, 'to_alipay_dict'):
                params['course_id'] = self.course_id.to_alipay_dict()
            else:
                params['course_id'] = self.course_id
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
        if self.enable_course_rule:
            if hasattr(self.enable_course_rule, 'to_alipay_dict'):
                params['enable_course_rule'] = self.enable_course_rule.to_alipay_dict()
            else:
                params['enable_course_rule'] = self.enable_course_rule
        if self.end_check_in:
            if hasattr(self.end_check_in, 'to_alipay_dict'):
                params['end_check_in'] = self.end_check_in.to_alipay_dict()
            else:
                params['end_check_in'] = self.end_check_in
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.manual_close:
            if hasattr(self.manual_close, 'to_alipay_dict'):
                params['manual_close'] = self.manual_close.to_alipay_dict()
            else:
                params['manual_close'] = self.manual_close
        if self.refresh_qr_code_frequency:
            if hasattr(self.refresh_qr_code_frequency, 'to_alipay_dict'):
                params['refresh_qr_code_frequency'] = self.refresh_qr_code_frequency.to_alipay_dict()
            else:
                params['refresh_qr_code_frequency'] = self.refresh_qr_code_frequency
        if self.roster_id:
            if hasattr(self.roster_id, 'to_alipay_dict'):
                params['roster_id'] = self.roster_id.to_alipay_dict()
            else:
                params['roster_id'] = self.roster_id
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateCourseCheckincodeCreateModel()
        if 'automatic_refresh' in d:
            o.automatic_refresh = d['automatic_refresh']
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'course_rule_id' in d:
            o.course_rule_id = d['course_rule_id']
        if 'course_rule_name' in d:
            o.course_rule_name = d['course_rule_name']
        if 'enable_course_rule' in d:
            o.enable_course_rule = d['enable_course_rule']
        if 'end_check_in' in d:
            o.end_check_in = d['end_check_in']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'manual_close' in d:
            o.manual_close = d['manual_close']
        if 'refresh_qr_code_frequency' in d:
            o.refresh_qr_code_frequency = d['refresh_qr_code_frequency']
        if 'roster_id' in d:
            o.roster_id = d['roster_id']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'status' in d:
            o.status = d['status']
        return o


