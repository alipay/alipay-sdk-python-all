#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAicsDevinTaskruleModifyModel(object):

    def __init__(self):
        self._enable_flag = None
        self._invalid_time = None
        self._remarks = None
        self._schedule_end_time = None
        self._schedule_start_time = None
        self._take_effect_time = None
        self._task_rules_code = None
        self._task_rules_detail = None
        self._task_rules_name = None
        self._tenant_id = None

    @property
    def enable_flag(self):
        return self._enable_flag

    @enable_flag.setter
    def enable_flag(self, value):
        self._enable_flag = value
    @property
    def invalid_time(self):
        return self._invalid_time

    @invalid_time.setter
    def invalid_time(self, value):
        self._invalid_time = value
    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value
    @property
    def schedule_end_time(self):
        return self._schedule_end_time

    @schedule_end_time.setter
    def schedule_end_time(self, value):
        self._schedule_end_time = value
    @property
    def schedule_start_time(self):
        return self._schedule_start_time

    @schedule_start_time.setter
    def schedule_start_time(self, value):
        self._schedule_start_time = value
    @property
    def take_effect_time(self):
        return self._take_effect_time

    @take_effect_time.setter
    def take_effect_time(self, value):
        self._take_effect_time = value
    @property
    def task_rules_code(self):
        return self._task_rules_code

    @task_rules_code.setter
    def task_rules_code(self, value):
        self._task_rules_code = value
    @property
    def task_rules_detail(self):
        return self._task_rules_detail

    @task_rules_detail.setter
    def task_rules_detail(self, value):
        self._task_rules_detail = value
    @property
    def task_rules_name(self):
        return self._task_rules_name

    @task_rules_name.setter
    def task_rules_name(self, value):
        self._task_rules_name = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enable_flag:
            if hasattr(self.enable_flag, 'to_alipay_dict'):
                params['enable_flag'] = self.enable_flag.to_alipay_dict()
            else:
                params['enable_flag'] = self.enable_flag
        if self.invalid_time:
            if hasattr(self.invalid_time, 'to_alipay_dict'):
                params['invalid_time'] = self.invalid_time.to_alipay_dict()
            else:
                params['invalid_time'] = self.invalid_time
        if self.remarks:
            if hasattr(self.remarks, 'to_alipay_dict'):
                params['remarks'] = self.remarks.to_alipay_dict()
            else:
                params['remarks'] = self.remarks
        if self.schedule_end_time:
            if hasattr(self.schedule_end_time, 'to_alipay_dict'):
                params['schedule_end_time'] = self.schedule_end_time.to_alipay_dict()
            else:
                params['schedule_end_time'] = self.schedule_end_time
        if self.schedule_start_time:
            if hasattr(self.schedule_start_time, 'to_alipay_dict'):
                params['schedule_start_time'] = self.schedule_start_time.to_alipay_dict()
            else:
                params['schedule_start_time'] = self.schedule_start_time
        if self.take_effect_time:
            if hasattr(self.take_effect_time, 'to_alipay_dict'):
                params['take_effect_time'] = self.take_effect_time.to_alipay_dict()
            else:
                params['take_effect_time'] = self.take_effect_time
        if self.task_rules_code:
            if hasattr(self.task_rules_code, 'to_alipay_dict'):
                params['task_rules_code'] = self.task_rules_code.to_alipay_dict()
            else:
                params['task_rules_code'] = self.task_rules_code
        if self.task_rules_detail:
            if hasattr(self.task_rules_detail, 'to_alipay_dict'):
                params['task_rules_detail'] = self.task_rules_detail.to_alipay_dict()
            else:
                params['task_rules_detail'] = self.task_rules_detail
        if self.task_rules_name:
            if hasattr(self.task_rules_name, 'to_alipay_dict'):
                params['task_rules_name'] = self.task_rules_name.to_alipay_dict()
            else:
                params['task_rules_name'] = self.task_rules_name
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAicsDevinTaskruleModifyModel()
        if 'enable_flag' in d:
            o.enable_flag = d['enable_flag']
        if 'invalid_time' in d:
            o.invalid_time = d['invalid_time']
        if 'remarks' in d:
            o.remarks = d['remarks']
        if 'schedule_end_time' in d:
            o.schedule_end_time = d['schedule_end_time']
        if 'schedule_start_time' in d:
            o.schedule_start_time = d['schedule_start_time']
        if 'take_effect_time' in d:
            o.take_effect_time = d['take_effect_time']
        if 'task_rules_code' in d:
            o.task_rules_code = d['task_rules_code']
        if 'task_rules_detail' in d:
            o.task_rules_detail = d['task_rules_detail']
        if 'task_rules_name' in d:
            o.task_rules_name = d['task_rules_name']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


