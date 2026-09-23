#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAicsDevinTaskModifyModel(object):

    def __init__(self):
        self._acquire_status = None
        self._ext_info = None
        self._last_acquire_status = None
        self._outbound_caller = None
        self._task_code = None
        self._task_name = None
        self._task_rules_code = None
        self._task_status = None
        self._tenant_id = None
        self._transfer_code = None
        self._version_on = None

    @property
    def acquire_status(self):
        return self._acquire_status

    @acquire_status.setter
    def acquire_status(self, value):
        self._acquire_status = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def last_acquire_status(self):
        return self._last_acquire_status

    @last_acquire_status.setter
    def last_acquire_status(self, value):
        self._last_acquire_status = value
    @property
    def outbound_caller(self):
        return self._outbound_caller

    @outbound_caller.setter
    def outbound_caller(self, value):
        self._outbound_caller = value
    @property
    def task_code(self):
        return self._task_code

    @task_code.setter
    def task_code(self, value):
        self._task_code = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_rules_code(self):
        return self._task_rules_code

    @task_rules_code.setter
    def task_rules_code(self, value):
        self._task_rules_code = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def transfer_code(self):
        return self._transfer_code

    @transfer_code.setter
    def transfer_code(self, value):
        self._transfer_code = value
    @property
    def version_on(self):
        return self._version_on

    @version_on.setter
    def version_on(self, value):
        self._version_on = value


    def to_alipay_dict(self):
        params = dict()
        if self.acquire_status:
            if hasattr(self.acquire_status, 'to_alipay_dict'):
                params['acquire_status'] = self.acquire_status.to_alipay_dict()
            else:
                params['acquire_status'] = self.acquire_status
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.last_acquire_status:
            if hasattr(self.last_acquire_status, 'to_alipay_dict'):
                params['last_acquire_status'] = self.last_acquire_status.to_alipay_dict()
            else:
                params['last_acquire_status'] = self.last_acquire_status
        if self.outbound_caller:
            if hasattr(self.outbound_caller, 'to_alipay_dict'):
                params['outbound_caller'] = self.outbound_caller.to_alipay_dict()
            else:
                params['outbound_caller'] = self.outbound_caller
        if self.task_code:
            if hasattr(self.task_code, 'to_alipay_dict'):
                params['task_code'] = self.task_code.to_alipay_dict()
            else:
                params['task_code'] = self.task_code
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_rules_code:
            if hasattr(self.task_rules_code, 'to_alipay_dict'):
                params['task_rules_code'] = self.task_rules_code.to_alipay_dict()
            else:
                params['task_rules_code'] = self.task_rules_code
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.transfer_code:
            if hasattr(self.transfer_code, 'to_alipay_dict'):
                params['transfer_code'] = self.transfer_code.to_alipay_dict()
            else:
                params['transfer_code'] = self.transfer_code
        if self.version_on:
            if hasattr(self.version_on, 'to_alipay_dict'):
                params['version_on'] = self.version_on.to_alipay_dict()
            else:
                params['version_on'] = self.version_on
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAicsDevinTaskModifyModel()
        if 'acquire_status' in d:
            o.acquire_status = d['acquire_status']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'last_acquire_status' in d:
            o.last_acquire_status = d['last_acquire_status']
        if 'outbound_caller' in d:
            o.outbound_caller = d['outbound_caller']
        if 'task_code' in d:
            o.task_code = d['task_code']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_rules_code' in d:
            o.task_rules_code = d['task_rules_code']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'transfer_code' in d:
            o.transfer_code = d['transfer_code']
        if 'version_on' in d:
            o.version_on = d['version_on']
        return o


