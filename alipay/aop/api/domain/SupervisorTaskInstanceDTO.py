#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IncentiveMode import IncentiveMode


class SupervisorTaskInstanceDTO(object):

    def __init__(self):
        self._incentive_mode = None
        self._receive_point = None
        self._task_desc = None
        self._task_end_time = None
        self._task_name = None
        self._task_rule_pic = None
        self._task_start_time = None
        self._template_status = None
        self._test_point_amount = None

    @property
    def incentive_mode(self):
        return self._incentive_mode

    @incentive_mode.setter
    def incentive_mode(self, value):
        if isinstance(value, IncentiveMode):
            self._incentive_mode = value
        else:
            self._incentive_mode = IncentiveMode.from_alipay_dict(value)
    @property
    def receive_point(self):
        return self._receive_point

    @receive_point.setter
    def receive_point(self, value):
        self._receive_point = value
    @property
    def task_desc(self):
        return self._task_desc

    @task_desc.setter
    def task_desc(self, value):
        self._task_desc = value
    @property
    def task_end_time(self):
        return self._task_end_time

    @task_end_time.setter
    def task_end_time(self, value):
        self._task_end_time = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_rule_pic(self):
        return self._task_rule_pic

    @task_rule_pic.setter
    def task_rule_pic(self, value):
        self._task_rule_pic = value
    @property
    def task_start_time(self):
        return self._task_start_time

    @task_start_time.setter
    def task_start_time(self, value):
        self._task_start_time = value
    @property
    def template_status(self):
        return self._template_status

    @template_status.setter
    def template_status(self, value):
        self._template_status = value
    @property
    def test_point_amount(self):
        return self._test_point_amount

    @test_point_amount.setter
    def test_point_amount(self, value):
        self._test_point_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.incentive_mode:
            if hasattr(self.incentive_mode, 'to_alipay_dict'):
                params['incentive_mode'] = self.incentive_mode.to_alipay_dict()
            else:
                params['incentive_mode'] = self.incentive_mode
        if self.receive_point:
            if hasattr(self.receive_point, 'to_alipay_dict'):
                params['receive_point'] = self.receive_point.to_alipay_dict()
            else:
                params['receive_point'] = self.receive_point
        if self.task_desc:
            if hasattr(self.task_desc, 'to_alipay_dict'):
                params['task_desc'] = self.task_desc.to_alipay_dict()
            else:
                params['task_desc'] = self.task_desc
        if self.task_end_time:
            if hasattr(self.task_end_time, 'to_alipay_dict'):
                params['task_end_time'] = self.task_end_time.to_alipay_dict()
            else:
                params['task_end_time'] = self.task_end_time
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_rule_pic:
            if hasattr(self.task_rule_pic, 'to_alipay_dict'):
                params['task_rule_pic'] = self.task_rule_pic.to_alipay_dict()
            else:
                params['task_rule_pic'] = self.task_rule_pic
        if self.task_start_time:
            if hasattr(self.task_start_time, 'to_alipay_dict'):
                params['task_start_time'] = self.task_start_time.to_alipay_dict()
            else:
                params['task_start_time'] = self.task_start_time
        if self.template_status:
            if hasattr(self.template_status, 'to_alipay_dict'):
                params['template_status'] = self.template_status.to_alipay_dict()
            else:
                params['template_status'] = self.template_status
        if self.test_point_amount:
            if hasattr(self.test_point_amount, 'to_alipay_dict'):
                params['test_point_amount'] = self.test_point_amount.to_alipay_dict()
            else:
                params['test_point_amount'] = self.test_point_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupervisorTaskInstanceDTO()
        if 'incentive_mode' in d:
            o.incentive_mode = d['incentive_mode']
        if 'receive_point' in d:
            o.receive_point = d['receive_point']
        if 'task_desc' in d:
            o.task_desc = d['task_desc']
        if 'task_end_time' in d:
            o.task_end_time = d['task_end_time']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_rule_pic' in d:
            o.task_rule_pic = d['task_rule_pic']
        if 'task_start_time' in d:
            o.task_start_time = d['task_start_time']
        if 'template_status' in d:
            o.template_status = d['template_status']
        if 'test_point_amount' in d:
            o.test_point_amount = d['test_point_amount']
        return o


