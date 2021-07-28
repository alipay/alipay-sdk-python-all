#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TaskOperationLog import TaskOperationLog


class AbnTaskInfo(object):

    def __init__(self):
        self._extens_info = None
        self._gmt_create = None
        self._gmt_modified = None
        self._handler_id = None
        self._handler_nick = None
        self._task_desc = None
        self._task_id = None
        self._task_level = None
        self._task_name = None
        self._task_operation_logs = None
        self._task_status = None
        self._task_type = None

    @property
    def extens_info(self):
        return self._extens_info

    @extens_info.setter
    def extens_info(self, value):
        self._extens_info = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def handler_id(self):
        return self._handler_id

    @handler_id.setter
    def handler_id(self, value):
        self._handler_id = value
    @property
    def handler_nick(self):
        return self._handler_nick

    @handler_nick.setter
    def handler_nick(self, value):
        self._handler_nick = value
    @property
    def task_desc(self):
        return self._task_desc

    @task_desc.setter
    def task_desc(self, value):
        self._task_desc = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_level(self):
        return self._task_level

    @task_level.setter
    def task_level(self, value):
        self._task_level = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_operation_logs(self):
        return self._task_operation_logs

    @task_operation_logs.setter
    def task_operation_logs(self, value):
        if isinstance(value, list):
            self._task_operation_logs = list()
            for i in value:
                if isinstance(i, TaskOperationLog):
                    self._task_operation_logs.append(i)
                else:
                    self._task_operation_logs.append(TaskOperationLog.from_alipay_dict(i))
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.extens_info:
            if hasattr(self.extens_info, 'to_alipay_dict'):
                params['extens_info'] = self.extens_info.to_alipay_dict()
            else:
                params['extens_info'] = self.extens_info
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.handler_id:
            if hasattr(self.handler_id, 'to_alipay_dict'):
                params['handler_id'] = self.handler_id.to_alipay_dict()
            else:
                params['handler_id'] = self.handler_id
        if self.handler_nick:
            if hasattr(self.handler_nick, 'to_alipay_dict'):
                params['handler_nick'] = self.handler_nick.to_alipay_dict()
            else:
                params['handler_nick'] = self.handler_nick
        if self.task_desc:
            if hasattr(self.task_desc, 'to_alipay_dict'):
                params['task_desc'] = self.task_desc.to_alipay_dict()
            else:
                params['task_desc'] = self.task_desc
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_level:
            if hasattr(self.task_level, 'to_alipay_dict'):
                params['task_level'] = self.task_level.to_alipay_dict()
            else:
                params['task_level'] = self.task_level
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_operation_logs:
            if isinstance(self.task_operation_logs, list):
                for i in range(0, len(self.task_operation_logs)):
                    element = self.task_operation_logs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_operation_logs[i] = element.to_alipay_dict()
            if hasattr(self.task_operation_logs, 'to_alipay_dict'):
                params['task_operation_logs'] = self.task_operation_logs.to_alipay_dict()
            else:
                params['task_operation_logs'] = self.task_operation_logs
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AbnTaskInfo()
        if 'extens_info' in d:
            o.extens_info = d['extens_info']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'handler_id' in d:
            o.handler_id = d['handler_id']
        if 'handler_nick' in d:
            o.handler_nick = d['handler_nick']
        if 'task_desc' in d:
            o.task_desc = d['task_desc']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_level' in d:
            o.task_level = d['task_level']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_operation_logs' in d:
            o.task_operation_logs = d['task_operation_logs']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'task_type' in d:
            o.task_type = d['task_type']
        return o


