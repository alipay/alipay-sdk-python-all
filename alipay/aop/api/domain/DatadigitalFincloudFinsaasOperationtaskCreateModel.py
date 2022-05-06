#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasOperationtaskCreateModel(object):

    def __init__(self):
        self._comment = None
        self._config = None
        self._operation_task_name = None
        self._operation_task_type = None
        self._plan_end_time = None
        self._plan_start_time = None
        self._status = None
        self._tenant_code = None
        self._user_id = None
        self._user_name = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value
    @property
    def operation_task_name(self):
        return self._operation_task_name

    @operation_task_name.setter
    def operation_task_name(self, value):
        self._operation_task_name = value
    @property
    def operation_task_type(self):
        return self._operation_task_type

    @operation_task_type.setter
    def operation_task_type(self, value):
        self._operation_task_type = value
    @property
    def plan_end_time(self):
        return self._plan_end_time

    @plan_end_time.setter
    def plan_end_time(self, value):
        self._plan_end_time = value
    @property
    def plan_start_time(self):
        return self._plan_start_time

    @plan_start_time.setter
    def plan_start_time(self, value):
        self._plan_start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.config:
            if hasattr(self.config, 'to_alipay_dict'):
                params['config'] = self.config.to_alipay_dict()
            else:
                params['config'] = self.config
        if self.operation_task_name:
            if hasattr(self.operation_task_name, 'to_alipay_dict'):
                params['operation_task_name'] = self.operation_task_name.to_alipay_dict()
            else:
                params['operation_task_name'] = self.operation_task_name
        if self.operation_task_type:
            if hasattr(self.operation_task_type, 'to_alipay_dict'):
                params['operation_task_type'] = self.operation_task_type.to_alipay_dict()
            else:
                params['operation_task_type'] = self.operation_task_type
        if self.plan_end_time:
            if hasattr(self.plan_end_time, 'to_alipay_dict'):
                params['plan_end_time'] = self.plan_end_time.to_alipay_dict()
            else:
                params['plan_end_time'] = self.plan_end_time
        if self.plan_start_time:
            if hasattr(self.plan_start_time, 'to_alipay_dict'):
                params['plan_start_time'] = self.plan_start_time.to_alipay_dict()
            else:
                params['plan_start_time'] = self.plan_start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasOperationtaskCreateModel()
        if 'comment' in d:
            o.comment = d['comment']
        if 'config' in d:
            o.config = d['config']
        if 'operation_task_name' in d:
            o.operation_task_name = d['operation_task_name']
        if 'operation_task_type' in d:
            o.operation_task_type = d['operation_task_type']
        if 'plan_end_time' in d:
            o.plan_end_time = d['plan_end_time']
        if 'plan_start_time' in d:
            o.plan_start_time = d['plan_start_time']
        if 'status' in d:
            o.status = d['status']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


