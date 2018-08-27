#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperatorBaseInfo(object):

    def __init__(self):
        self._dept_id = None
        self._dept_path = None
        self._mobile = None
        self._nick_name = None
        self._operator_id = None
        self._operator_name = None
        self._operator_type = None
        self._role_code = None
        self._role_id = None
        self._role_name = None
        self._status = None

    @property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value
    @property
    def dept_path(self):
        return self._dept_path

    @dept_path.setter
    def dept_path(self, value):
        self._dept_path = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def role_code(self):
        return self._role_code

    @role_code.setter
    def role_code(self, value):
        self._role_code = value
    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        self._role_id = value
    @property
    def role_name(self):
        return self._role_name

    @role_name.setter
    def role_name(self, value):
        self._role_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.dept_id:
            if hasattr(self.dept_id, 'to_alipay_dict'):
                params['dept_id'] = self.dept_id.to_alipay_dict()
            else:
                params['dept_id'] = self.dept_id
        if self.dept_path:
            if hasattr(self.dept_path, 'to_alipay_dict'):
                params['dept_path'] = self.dept_path.to_alipay_dict()
            else:
                params['dept_path'] = self.dept_path
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.role_code:
            if hasattr(self.role_code, 'to_alipay_dict'):
                params['role_code'] = self.role_code.to_alipay_dict()
            else:
                params['role_code'] = self.role_code
        if self.role_id:
            if hasattr(self.role_id, 'to_alipay_dict'):
                params['role_id'] = self.role_id.to_alipay_dict()
            else:
                params['role_id'] = self.role_id
        if self.role_name:
            if hasattr(self.role_name, 'to_alipay_dict'):
                params['role_name'] = self.role_name.to_alipay_dict()
            else:
                params['role_name'] = self.role_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperatorBaseInfo()
        if 'dept_id' in d:
            o.dept_id = d['dept_id']
        if 'dept_path' in d:
            o.dept_path = d['dept_path']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'role_code' in d:
            o.role_code = d['role_code']
        if 'role_id' in d:
            o.role_id = d['role_id']
        if 'role_name' in d:
            o.role_name = d['role_name']
        if 'status' in d:
            o.status = d['status']
        return o


