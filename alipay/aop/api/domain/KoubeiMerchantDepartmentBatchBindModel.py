#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SimpleOperatorModel import SimpleOperatorModel


class KoubeiMerchantDepartmentBatchBindModel(object):

    def __init__(self):
        self._auth_code = None
        self._dept_id = None
        self._dept_type = None
        self._operator_list = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value
    @property
    def dept_type(self):
        return self._dept_type

    @dept_type.setter
    def dept_type(self, value):
        self._dept_type = value
    @property
    def operator_list(self):
        return self._operator_list

    @operator_list.setter
    def operator_list(self, value):
        if isinstance(value, list):
            self._operator_list = list()
            for i in value:
                if isinstance(i, SimpleOperatorModel):
                    self._operator_list.append(i)
                else:
                    self._operator_list.append(SimpleOperatorModel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.dept_id:
            if hasattr(self.dept_id, 'to_alipay_dict'):
                params['dept_id'] = self.dept_id.to_alipay_dict()
            else:
                params['dept_id'] = self.dept_id
        if self.dept_type:
            if hasattr(self.dept_type, 'to_alipay_dict'):
                params['dept_type'] = self.dept_type.to_alipay_dict()
            else:
                params['dept_type'] = self.dept_type
        if self.operator_list:
            if isinstance(self.operator_list, list):
                for i in range(0, len(self.operator_list)):
                    element = self.operator_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operator_list[i] = element.to_alipay_dict()
            if hasattr(self.operator_list, 'to_alipay_dict'):
                params['operator_list'] = self.operator_list.to_alipay_dict()
            else:
                params['operator_list'] = self.operator_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMerchantDepartmentBatchBindModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'dept_id' in d:
            o.dept_id = d['dept_id']
        if 'dept_type' in d:
            o.dept_type = d['dept_type']
        if 'operator_list' in d:
            o.operator_list = d['operator_list']
        return o


