#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskInstanceInfo(object):

    def __init__(self):
        self._current_indicator = None
        self._incentive_mode = None
        self._incentive_rule = None
        self._max_incentive_count = None
        self._published_point_amount = None
        self._status = None
        self._target_indicator = None
        self._task_end_time = None
        self._task_instance_id = None
        self._task_logo = None
        self._task_name = None
        self._task_start_time = None
        self._task_template_id = None
        self._task_type = None
        self._total_point_amount = None
        self._unexchange_point_amount = None

    @property
    def current_indicator(self):
        return self._current_indicator

    @current_indicator.setter
    def current_indicator(self, value):
        self._current_indicator = value
    @property
    def incentive_mode(self):
        return self._incentive_mode

    @incentive_mode.setter
    def incentive_mode(self, value):
        self._incentive_mode = value
    @property
    def incentive_rule(self):
        return self._incentive_rule

    @incentive_rule.setter
    def incentive_rule(self, value):
        self._incentive_rule = value
    @property
    def max_incentive_count(self):
        return self._max_incentive_count

    @max_incentive_count.setter
    def max_incentive_count(self, value):
        self._max_incentive_count = value
    @property
    def published_point_amount(self):
        return self._published_point_amount

    @published_point_amount.setter
    def published_point_amount(self, value):
        self._published_point_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target_indicator(self):
        return self._target_indicator

    @target_indicator.setter
    def target_indicator(self, value):
        self._target_indicator = value
    @property
    def task_end_time(self):
        return self._task_end_time

    @task_end_time.setter
    def task_end_time(self, value):
        self._task_end_time = value
    @property
    def task_instance_id(self):
        return self._task_instance_id

    @task_instance_id.setter
    def task_instance_id(self, value):
        self._task_instance_id = value
    @property
    def task_logo(self):
        return self._task_logo

    @task_logo.setter
    def task_logo(self, value):
        self._task_logo = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_start_time(self):
        return self._task_start_time

    @task_start_time.setter
    def task_start_time(self, value):
        self._task_start_time = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value
    @property
    def total_point_amount(self):
        return self._total_point_amount

    @total_point_amount.setter
    def total_point_amount(self, value):
        self._total_point_amount = value
    @property
    def unexchange_point_amount(self):
        return self._unexchange_point_amount

    @unexchange_point_amount.setter
    def unexchange_point_amount(self, value):
        self._unexchange_point_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_indicator:
            if hasattr(self.current_indicator, 'to_alipay_dict'):
                params['current_indicator'] = self.current_indicator.to_alipay_dict()
            else:
                params['current_indicator'] = self.current_indicator
        if self.incentive_mode:
            if hasattr(self.incentive_mode, 'to_alipay_dict'):
                params['incentive_mode'] = self.incentive_mode.to_alipay_dict()
            else:
                params['incentive_mode'] = self.incentive_mode
        if self.incentive_rule:
            if hasattr(self.incentive_rule, 'to_alipay_dict'):
                params['incentive_rule'] = self.incentive_rule.to_alipay_dict()
            else:
                params['incentive_rule'] = self.incentive_rule
        if self.max_incentive_count:
            if hasattr(self.max_incentive_count, 'to_alipay_dict'):
                params['max_incentive_count'] = self.max_incentive_count.to_alipay_dict()
            else:
                params['max_incentive_count'] = self.max_incentive_count
        if self.published_point_amount:
            if hasattr(self.published_point_amount, 'to_alipay_dict'):
                params['published_point_amount'] = self.published_point_amount.to_alipay_dict()
            else:
                params['published_point_amount'] = self.published_point_amount
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.target_indicator:
            if hasattr(self.target_indicator, 'to_alipay_dict'):
                params['target_indicator'] = self.target_indicator.to_alipay_dict()
            else:
                params['target_indicator'] = self.target_indicator
        if self.task_end_time:
            if hasattr(self.task_end_time, 'to_alipay_dict'):
                params['task_end_time'] = self.task_end_time.to_alipay_dict()
            else:
                params['task_end_time'] = self.task_end_time
        if self.task_instance_id:
            if hasattr(self.task_instance_id, 'to_alipay_dict'):
                params['task_instance_id'] = self.task_instance_id.to_alipay_dict()
            else:
                params['task_instance_id'] = self.task_instance_id
        if self.task_logo:
            if hasattr(self.task_logo, 'to_alipay_dict'):
                params['task_logo'] = self.task_logo.to_alipay_dict()
            else:
                params['task_logo'] = self.task_logo
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_start_time:
            if hasattr(self.task_start_time, 'to_alipay_dict'):
                params['task_start_time'] = self.task_start_time.to_alipay_dict()
            else:
                params['task_start_time'] = self.task_start_time
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        if self.total_point_amount:
            if hasattr(self.total_point_amount, 'to_alipay_dict'):
                params['total_point_amount'] = self.total_point_amount.to_alipay_dict()
            else:
                params['total_point_amount'] = self.total_point_amount
        if self.unexchange_point_amount:
            if hasattr(self.unexchange_point_amount, 'to_alipay_dict'):
                params['unexchange_point_amount'] = self.unexchange_point_amount.to_alipay_dict()
            else:
                params['unexchange_point_amount'] = self.unexchange_point_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskInstanceInfo()
        if 'current_indicator' in d:
            o.current_indicator = d['current_indicator']
        if 'incentive_mode' in d:
            o.incentive_mode = d['incentive_mode']
        if 'incentive_rule' in d:
            o.incentive_rule = d['incentive_rule']
        if 'max_incentive_count' in d:
            o.max_incentive_count = d['max_incentive_count']
        if 'published_point_amount' in d:
            o.published_point_amount = d['published_point_amount']
        if 'status' in d:
            o.status = d['status']
        if 'target_indicator' in d:
            o.target_indicator = d['target_indicator']
        if 'task_end_time' in d:
            o.task_end_time = d['task_end_time']
        if 'task_instance_id' in d:
            o.task_instance_id = d['task_instance_id']
        if 'task_logo' in d:
            o.task_logo = d['task_logo']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_start_time' in d:
            o.task_start_time = d['task_start_time']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'total_point_amount' in d:
            o.total_point_amount = d['total_point_amount']
        if 'unexchange_point_amount' in d:
            o.unexchange_point_amount = d['unexchange_point_amount']
        return o


