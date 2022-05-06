#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceApccenterAlgorithmbaseinfoModifyModel(object):

    def __init__(self):
        self._platform_algorithm_code = None
        self._platform_algorithm_create_time = None
        self._platform_algorithm_desc = None
        self._platform_algorithm_last_iteration_code = None
        self._platform_algorithm_last_iteration_op_user_emp_no = None
        self._platform_algorithm_modify_time = None
        self._platform_algorithm_name = None
        self._platform_algorithm_owner_emp_no = None
        self._platform_algorithm_source = None
        self._platform_algorithm_status = None

    @property
    def platform_algorithm_code(self):
        return self._platform_algorithm_code

    @platform_algorithm_code.setter
    def platform_algorithm_code(self, value):
        self._platform_algorithm_code = value
    @property
    def platform_algorithm_create_time(self):
        return self._platform_algorithm_create_time

    @platform_algorithm_create_time.setter
    def platform_algorithm_create_time(self, value):
        self._platform_algorithm_create_time = value
    @property
    def platform_algorithm_desc(self):
        return self._platform_algorithm_desc

    @platform_algorithm_desc.setter
    def platform_algorithm_desc(self, value):
        self._platform_algorithm_desc = value
    @property
    def platform_algorithm_last_iteration_code(self):
        return self._platform_algorithm_last_iteration_code

    @platform_algorithm_last_iteration_code.setter
    def platform_algorithm_last_iteration_code(self, value):
        self._platform_algorithm_last_iteration_code = value
    @property
    def platform_algorithm_last_iteration_op_user_emp_no(self):
        return self._platform_algorithm_last_iteration_op_user_emp_no

    @platform_algorithm_last_iteration_op_user_emp_no.setter
    def platform_algorithm_last_iteration_op_user_emp_no(self, value):
        self._platform_algorithm_last_iteration_op_user_emp_no = value
    @property
    def platform_algorithm_modify_time(self):
        return self._platform_algorithm_modify_time

    @platform_algorithm_modify_time.setter
    def platform_algorithm_modify_time(self, value):
        self._platform_algorithm_modify_time = value
    @property
    def platform_algorithm_name(self):
        return self._platform_algorithm_name

    @platform_algorithm_name.setter
    def platform_algorithm_name(self, value):
        self._platform_algorithm_name = value
    @property
    def platform_algorithm_owner_emp_no(self):
        return self._platform_algorithm_owner_emp_no

    @platform_algorithm_owner_emp_no.setter
    def platform_algorithm_owner_emp_no(self, value):
        self._platform_algorithm_owner_emp_no = value
    @property
    def platform_algorithm_source(self):
        return self._platform_algorithm_source

    @platform_algorithm_source.setter
    def platform_algorithm_source(self, value):
        self._platform_algorithm_source = value
    @property
    def platform_algorithm_status(self):
        return self._platform_algorithm_status

    @platform_algorithm_status.setter
    def platform_algorithm_status(self, value):
        self._platform_algorithm_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.platform_algorithm_code:
            if hasattr(self.platform_algorithm_code, 'to_alipay_dict'):
                params['platform_algorithm_code'] = self.platform_algorithm_code.to_alipay_dict()
            else:
                params['platform_algorithm_code'] = self.platform_algorithm_code
        if self.platform_algorithm_create_time:
            if hasattr(self.platform_algorithm_create_time, 'to_alipay_dict'):
                params['platform_algorithm_create_time'] = self.platform_algorithm_create_time.to_alipay_dict()
            else:
                params['platform_algorithm_create_time'] = self.platform_algorithm_create_time
        if self.platform_algorithm_desc:
            if hasattr(self.platform_algorithm_desc, 'to_alipay_dict'):
                params['platform_algorithm_desc'] = self.platform_algorithm_desc.to_alipay_dict()
            else:
                params['platform_algorithm_desc'] = self.platform_algorithm_desc
        if self.platform_algorithm_last_iteration_code:
            if hasattr(self.platform_algorithm_last_iteration_code, 'to_alipay_dict'):
                params['platform_algorithm_last_iteration_code'] = self.platform_algorithm_last_iteration_code.to_alipay_dict()
            else:
                params['platform_algorithm_last_iteration_code'] = self.platform_algorithm_last_iteration_code
        if self.platform_algorithm_last_iteration_op_user_emp_no:
            if hasattr(self.platform_algorithm_last_iteration_op_user_emp_no, 'to_alipay_dict'):
                params['platform_algorithm_last_iteration_op_user_emp_no'] = self.platform_algorithm_last_iteration_op_user_emp_no.to_alipay_dict()
            else:
                params['platform_algorithm_last_iteration_op_user_emp_no'] = self.platform_algorithm_last_iteration_op_user_emp_no
        if self.platform_algorithm_modify_time:
            if hasattr(self.platform_algorithm_modify_time, 'to_alipay_dict'):
                params['platform_algorithm_modify_time'] = self.platform_algorithm_modify_time.to_alipay_dict()
            else:
                params['platform_algorithm_modify_time'] = self.platform_algorithm_modify_time
        if self.platform_algorithm_name:
            if hasattr(self.platform_algorithm_name, 'to_alipay_dict'):
                params['platform_algorithm_name'] = self.platform_algorithm_name.to_alipay_dict()
            else:
                params['platform_algorithm_name'] = self.platform_algorithm_name
        if self.platform_algorithm_owner_emp_no:
            if hasattr(self.platform_algorithm_owner_emp_no, 'to_alipay_dict'):
                params['platform_algorithm_owner_emp_no'] = self.platform_algorithm_owner_emp_no.to_alipay_dict()
            else:
                params['platform_algorithm_owner_emp_no'] = self.platform_algorithm_owner_emp_no
        if self.platform_algorithm_source:
            if hasattr(self.platform_algorithm_source, 'to_alipay_dict'):
                params['platform_algorithm_source'] = self.platform_algorithm_source.to_alipay_dict()
            else:
                params['platform_algorithm_source'] = self.platform_algorithm_source
        if self.platform_algorithm_status:
            if hasattr(self.platform_algorithm_status, 'to_alipay_dict'):
                params['platform_algorithm_status'] = self.platform_algorithm_status.to_alipay_dict()
            else:
                params['platform_algorithm_status'] = self.platform_algorithm_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceApccenterAlgorithmbaseinfoModifyModel()
        if 'platform_algorithm_code' in d:
            o.platform_algorithm_code = d['platform_algorithm_code']
        if 'platform_algorithm_create_time' in d:
            o.platform_algorithm_create_time = d['platform_algorithm_create_time']
        if 'platform_algorithm_desc' in d:
            o.platform_algorithm_desc = d['platform_algorithm_desc']
        if 'platform_algorithm_last_iteration_code' in d:
            o.platform_algorithm_last_iteration_code = d['platform_algorithm_last_iteration_code']
        if 'platform_algorithm_last_iteration_op_user_emp_no' in d:
            o.platform_algorithm_last_iteration_op_user_emp_no = d['platform_algorithm_last_iteration_op_user_emp_no']
        if 'platform_algorithm_modify_time' in d:
            o.platform_algorithm_modify_time = d['platform_algorithm_modify_time']
        if 'platform_algorithm_name' in d:
            o.platform_algorithm_name = d['platform_algorithm_name']
        if 'platform_algorithm_owner_emp_no' in d:
            o.platform_algorithm_owner_emp_no = d['platform_algorithm_owner_emp_no']
        if 'platform_algorithm_source' in d:
            o.platform_algorithm_source = d['platform_algorithm_source']
        if 'platform_algorithm_status' in d:
            o.platform_algorithm_status = d['platform_algorithm_status']
        return o


