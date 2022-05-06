#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasOperationtaskQueryModel(object):

    def __init__(self):
        self._operation_task_id = None
        self._tenant_code = None

    @property
    def operation_task_id(self):
        return self._operation_task_id

    @operation_task_id.setter
    def operation_task_id(self, value):
        self._operation_task_id = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.operation_task_id:
            if hasattr(self.operation_task_id, 'to_alipay_dict'):
                params['operation_task_id'] = self.operation_task_id.to_alipay_dict()
            else:
                params['operation_task_id'] = self.operation_task_id
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasOperationtaskQueryModel()
        if 'operation_task_id' in d:
            o.operation_task_id = d['operation_task_id']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o


