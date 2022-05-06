#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasOperationtaskBatchqueryModel(object):

    def __init__(self):
        self._execution_time = None
        self._operation_task_name = None
        self._page_num = None
        self._page_size = None
        self._status = None
        self._tenant_code = None
        self._user_ids = None
        self._user_name = None

    @property
    def execution_time(self):
        return self._execution_time

    @execution_time.setter
    def execution_time(self, value):
        self._execution_time = value
    @property
    def operation_task_name(self):
        return self._operation_task_name

    @operation_task_name.setter
    def operation_task_name(self, value):
        self._operation_task_name = value
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
    def user_ids(self):
        return self._user_ids

    @user_ids.setter
    def user_ids(self, value):
        self._user_ids = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.execution_time:
            if hasattr(self.execution_time, 'to_alipay_dict'):
                params['execution_time'] = self.execution_time.to_alipay_dict()
            else:
                params['execution_time'] = self.execution_time
        if self.operation_task_name:
            if hasattr(self.operation_task_name, 'to_alipay_dict'):
                params['operation_task_name'] = self.operation_task_name.to_alipay_dict()
            else:
                params['operation_task_name'] = self.operation_task_name
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
        if self.user_ids:
            if hasattr(self.user_ids, 'to_alipay_dict'):
                params['user_ids'] = self.user_ids.to_alipay_dict()
            else:
                params['user_ids'] = self.user_ids
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
        o = DatadigitalFincloudFinsaasOperationtaskBatchqueryModel()
        if 'execution_time' in d:
            o.execution_time = d['execution_time']
        if 'operation_task_name' in d:
            o.operation_task_name = d['operation_task_name']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'status' in d:
            o.status = d['status']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        if 'user_ids' in d:
            o.user_ids = d['user_ids']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


