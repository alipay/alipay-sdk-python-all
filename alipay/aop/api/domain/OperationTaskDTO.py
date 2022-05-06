#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperationTaskDTO(object):

    def __init__(self):
        self._comment = None
        self._operation_task_id = None
        self._operation_task_name = None
        self._operation_task_type = None
        self._plan_end_time = None
        self._plan_start_time = None
        self._reject_comment = None
        self._status = None
        self._status_name = None
        self._user_id = None
        self._user_name = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def operation_task_id(self):
        return self._operation_task_id

    @operation_task_id.setter
    def operation_task_id(self, value):
        self._operation_task_id = value
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
    def reject_comment(self):
        return self._reject_comment

    @reject_comment.setter
    def reject_comment(self, value):
        self._reject_comment = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_name(self):
        return self._status_name

    @status_name.setter
    def status_name(self, value):
        self._status_name = value
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
        if self.operation_task_id:
            if hasattr(self.operation_task_id, 'to_alipay_dict'):
                params['operation_task_id'] = self.operation_task_id.to_alipay_dict()
            else:
                params['operation_task_id'] = self.operation_task_id
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
        if self.reject_comment:
            if hasattr(self.reject_comment, 'to_alipay_dict'):
                params['reject_comment'] = self.reject_comment.to_alipay_dict()
            else:
                params['reject_comment'] = self.reject_comment
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_name:
            if hasattr(self.status_name, 'to_alipay_dict'):
                params['status_name'] = self.status_name.to_alipay_dict()
            else:
                params['status_name'] = self.status_name
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
        o = OperationTaskDTO()
        if 'comment' in d:
            o.comment = d['comment']
        if 'operation_task_id' in d:
            o.operation_task_id = d['operation_task_id']
        if 'operation_task_name' in d:
            o.operation_task_name = d['operation_task_name']
        if 'operation_task_type' in d:
            o.operation_task_type = d['operation_task_type']
        if 'plan_end_time' in d:
            o.plan_end_time = d['plan_end_time']
        if 'plan_start_time' in d:
            o.plan_start_time = d['plan_start_time']
        if 'reject_comment' in d:
            o.reject_comment = d['reject_comment']
        if 'status' in d:
            o.status = d['status']
        if 'status_name' in d:
            o.status_name = d['status_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


