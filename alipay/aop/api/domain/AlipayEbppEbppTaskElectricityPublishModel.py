#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEbppTaskElectricityPublishModel(object):

    def __init__(self):
        self._active_end_time = None
        self._active_start_time = None
        self._have_reward = None
        self._is_test = None
        self._out_task_id = None
        self._rule_info = None
        self._task_active_data = None
        self._task_active_range = None
        self._task_active_target = None
        self._task_event_no = None
        self._task_join_limit_time = None
        self._task_province_code = None
        self._task_response_level = None
        self._task_type = None
        self._tempreture_active_data = None

    @property
    def active_end_time(self):
        return self._active_end_time

    @active_end_time.setter
    def active_end_time(self, value):
        self._active_end_time = value
    @property
    def active_start_time(self):
        return self._active_start_time

    @active_start_time.setter
    def active_start_time(self, value):
        self._active_start_time = value
    @property
    def have_reward(self):
        return self._have_reward

    @have_reward.setter
    def have_reward(self, value):
        self._have_reward = value
    @property
    def is_test(self):
        return self._is_test

    @is_test.setter
    def is_test(self, value):
        self._is_test = value
    @property
    def out_task_id(self):
        return self._out_task_id

    @out_task_id.setter
    def out_task_id(self, value):
        self._out_task_id = value
    @property
    def rule_info(self):
        return self._rule_info

    @rule_info.setter
    def rule_info(self, value):
        self._rule_info = value
    @property
    def task_active_data(self):
        return self._task_active_data

    @task_active_data.setter
    def task_active_data(self, value):
        self._task_active_data = value
    @property
    def task_active_range(self):
        return self._task_active_range

    @task_active_range.setter
    def task_active_range(self, value):
        self._task_active_range = value
    @property
    def task_active_target(self):
        return self._task_active_target

    @task_active_target.setter
    def task_active_target(self, value):
        self._task_active_target = value
    @property
    def task_event_no(self):
        return self._task_event_no

    @task_event_no.setter
    def task_event_no(self, value):
        self._task_event_no = value
    @property
    def task_join_limit_time(self):
        return self._task_join_limit_time

    @task_join_limit_time.setter
    def task_join_limit_time(self, value):
        self._task_join_limit_time = value
    @property
    def task_province_code(self):
        return self._task_province_code

    @task_province_code.setter
    def task_province_code(self, value):
        self._task_province_code = value
    @property
    def task_response_level(self):
        return self._task_response_level

    @task_response_level.setter
    def task_response_level(self, value):
        self._task_response_level = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value
    @property
    def tempreture_active_data(self):
        return self._tempreture_active_data

    @tempreture_active_data.setter
    def tempreture_active_data(self, value):
        self._tempreture_active_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_end_time:
            if hasattr(self.active_end_time, 'to_alipay_dict'):
                params['active_end_time'] = self.active_end_time.to_alipay_dict()
            else:
                params['active_end_time'] = self.active_end_time
        if self.active_start_time:
            if hasattr(self.active_start_time, 'to_alipay_dict'):
                params['active_start_time'] = self.active_start_time.to_alipay_dict()
            else:
                params['active_start_time'] = self.active_start_time
        if self.have_reward:
            if hasattr(self.have_reward, 'to_alipay_dict'):
                params['have_reward'] = self.have_reward.to_alipay_dict()
            else:
                params['have_reward'] = self.have_reward
        if self.is_test:
            if hasattr(self.is_test, 'to_alipay_dict'):
                params['is_test'] = self.is_test.to_alipay_dict()
            else:
                params['is_test'] = self.is_test
        if self.out_task_id:
            if hasattr(self.out_task_id, 'to_alipay_dict'):
                params['out_task_id'] = self.out_task_id.to_alipay_dict()
            else:
                params['out_task_id'] = self.out_task_id
        if self.rule_info:
            if hasattr(self.rule_info, 'to_alipay_dict'):
                params['rule_info'] = self.rule_info.to_alipay_dict()
            else:
                params['rule_info'] = self.rule_info
        if self.task_active_data:
            if hasattr(self.task_active_data, 'to_alipay_dict'):
                params['task_active_data'] = self.task_active_data.to_alipay_dict()
            else:
                params['task_active_data'] = self.task_active_data
        if self.task_active_range:
            if hasattr(self.task_active_range, 'to_alipay_dict'):
                params['task_active_range'] = self.task_active_range.to_alipay_dict()
            else:
                params['task_active_range'] = self.task_active_range
        if self.task_active_target:
            if hasattr(self.task_active_target, 'to_alipay_dict'):
                params['task_active_target'] = self.task_active_target.to_alipay_dict()
            else:
                params['task_active_target'] = self.task_active_target
        if self.task_event_no:
            if hasattr(self.task_event_no, 'to_alipay_dict'):
                params['task_event_no'] = self.task_event_no.to_alipay_dict()
            else:
                params['task_event_no'] = self.task_event_no
        if self.task_join_limit_time:
            if hasattr(self.task_join_limit_time, 'to_alipay_dict'):
                params['task_join_limit_time'] = self.task_join_limit_time.to_alipay_dict()
            else:
                params['task_join_limit_time'] = self.task_join_limit_time
        if self.task_province_code:
            if hasattr(self.task_province_code, 'to_alipay_dict'):
                params['task_province_code'] = self.task_province_code.to_alipay_dict()
            else:
                params['task_province_code'] = self.task_province_code
        if self.task_response_level:
            if hasattr(self.task_response_level, 'to_alipay_dict'):
                params['task_response_level'] = self.task_response_level.to_alipay_dict()
            else:
                params['task_response_level'] = self.task_response_level
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        if self.tempreture_active_data:
            if hasattr(self.tempreture_active_data, 'to_alipay_dict'):
                params['tempreture_active_data'] = self.tempreture_active_data.to_alipay_dict()
            else:
                params['tempreture_active_data'] = self.tempreture_active_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppEbppTaskElectricityPublishModel()
        if 'active_end_time' in d:
            o.active_end_time = d['active_end_time']
        if 'active_start_time' in d:
            o.active_start_time = d['active_start_time']
        if 'have_reward' in d:
            o.have_reward = d['have_reward']
        if 'is_test' in d:
            o.is_test = d['is_test']
        if 'out_task_id' in d:
            o.out_task_id = d['out_task_id']
        if 'rule_info' in d:
            o.rule_info = d['rule_info']
        if 'task_active_data' in d:
            o.task_active_data = d['task_active_data']
        if 'task_active_range' in d:
            o.task_active_range = d['task_active_range']
        if 'task_active_target' in d:
            o.task_active_target = d['task_active_target']
        if 'task_event_no' in d:
            o.task_event_no = d['task_event_no']
        if 'task_join_limit_time' in d:
            o.task_join_limit_time = d['task_join_limit_time']
        if 'task_province_code' in d:
            o.task_province_code = d['task_province_code']
        if 'task_response_level' in d:
            o.task_response_level = d['task_response_level']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'tempreture_active_data' in d:
            o.tempreture_active_data = d['tempreture_active_data']
        return o


