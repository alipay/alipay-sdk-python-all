#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAicsDevinTaskCreateModel(object):

    def __init__(self):
        self._ext_info = None
        self._outbound_caller = None
        self._task_code = None
        self._task_name = None
        self._task_rules_code = None
        self._task_status = None
        self._task_transfer_type = None
        self._task_type = None
        self._tenant_id = None
        self._transfer_code = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
    def task_transfer_type(self):
        return self._task_transfer_type

    @task_transfer_type.setter
    def task_transfer_type(self, value):
        self._task_transfer_type = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        if self.task_transfer_type:
            if hasattr(self.task_transfer_type, 'to_alipay_dict'):
                params['task_transfer_type'] = self.task_transfer_type.to_alipay_dict()
            else:
                params['task_transfer_type'] = self.task_transfer_type
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAicsDevinTaskCreateModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
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
        if 'task_transfer_type' in d:
            o.task_transfer_type = d['task_transfer_type']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'transfer_code' in d:
            o.transfer_code = d['transfer_code']
        return o


