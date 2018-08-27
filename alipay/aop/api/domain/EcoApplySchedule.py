#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcoApplySchedule(object):

    def __init__(self):
        self._audit_comment = None
        self._audit_time = None
        self._edit_flag = None
        self._order_no = None
        self._order_num = None
        self._status = None
        self._status_desc = None
        self._step = None
        self._step_desc = None

    @property
    def audit_comment(self):
        return self._audit_comment

    @audit_comment.setter
    def audit_comment(self, value):
        self._audit_comment = value
    @property
    def audit_time(self):
        return self._audit_time

    @audit_time.setter
    def audit_time(self, value):
        self._audit_time = value
    @property
    def edit_flag(self):
        return self._edit_flag

    @edit_flag.setter
    def edit_flag(self, value):
        self._edit_flag = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_num(self):
        return self._order_num

    @order_num.setter
    def order_num(self, value):
        self._order_num = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value
    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value
    @property
    def step_desc(self):
        return self._step_desc

    @step_desc.setter
    def step_desc(self, value):
        self._step_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_comment:
            if hasattr(self.audit_comment, 'to_alipay_dict'):
                params['audit_comment'] = self.audit_comment.to_alipay_dict()
            else:
                params['audit_comment'] = self.audit_comment
        if self.audit_time:
            if hasattr(self.audit_time, 'to_alipay_dict'):
                params['audit_time'] = self.audit_time.to_alipay_dict()
            else:
                params['audit_time'] = self.audit_time
        if self.edit_flag:
            if hasattr(self.edit_flag, 'to_alipay_dict'):
                params['edit_flag'] = self.edit_flag.to_alipay_dict()
            else:
                params['edit_flag'] = self.edit_flag
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_num:
            if hasattr(self.order_num, 'to_alipay_dict'):
                params['order_num'] = self.order_num.to_alipay_dict()
            else:
                params['order_num'] = self.order_num
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        if self.step:
            if hasattr(self.step, 'to_alipay_dict'):
                params['step'] = self.step.to_alipay_dict()
            else:
                params['step'] = self.step
        if self.step_desc:
            if hasattr(self.step_desc, 'to_alipay_dict'):
                params['step_desc'] = self.step_desc.to_alipay_dict()
            else:
                params['step_desc'] = self.step_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcoApplySchedule()
        if 'audit_comment' in d:
            o.audit_comment = d['audit_comment']
        if 'audit_time' in d:
            o.audit_time = d['audit_time']
        if 'edit_flag' in d:
            o.edit_flag = d['edit_flag']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_num' in d:
            o.order_num = d['order_num']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        if 'step' in d:
            o.step = d['step']
        if 'step_desc' in d:
            o.step_desc = d['step_desc']
        return o


