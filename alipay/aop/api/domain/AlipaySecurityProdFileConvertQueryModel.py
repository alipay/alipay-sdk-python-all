#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdFileConvertQueryModel(object):

    def __init__(self):
        self._convert_task_id = None
        self._emp_id = None
        self._source_system_id = None
        self._target_file_path = None
        self._tenant = None

    @property
    def convert_task_id(self):
        return self._convert_task_id

    @convert_task_id.setter
    def convert_task_id(self, value):
        self._convert_task_id = value
    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def target_file_path(self):
        return self._target_file_path

    @target_file_path.setter
    def target_file_path(self, value):
        self._target_file_path = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.convert_task_id:
            if hasattr(self.convert_task_id, 'to_alipay_dict'):
                params['convert_task_id'] = self.convert_task_id.to_alipay_dict()
            else:
                params['convert_task_id'] = self.convert_task_id
        if self.emp_id:
            if hasattr(self.emp_id, 'to_alipay_dict'):
                params['emp_id'] = self.emp_id.to_alipay_dict()
            else:
                params['emp_id'] = self.emp_id
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        if self.target_file_path:
            if hasattr(self.target_file_path, 'to_alipay_dict'):
                params['target_file_path'] = self.target_file_path.to_alipay_dict()
            else:
                params['target_file_path'] = self.target_file_path
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdFileConvertQueryModel()
        if 'convert_task_id' in d:
            o.convert_task_id = d['convert_task_id']
        if 'emp_id' in d:
            o.emp_id = d['emp_id']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'target_file_path' in d:
            o.target_file_path = d['target_file_path']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


