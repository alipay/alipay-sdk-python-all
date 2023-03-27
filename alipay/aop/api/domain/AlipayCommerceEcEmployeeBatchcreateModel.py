#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EmployeeBatchAddDTO import EmployeeBatchAddDTO


class AlipayCommerceEcEmployeeBatchcreateModel(object):

    def __init__(self):
        self._employee_list = None
        self._enterprise_id = None

    @property
    def employee_list(self):
        return self._employee_list

    @employee_list.setter
    def employee_list(self, value):
        if isinstance(value, list):
            self._employee_list = list()
            for i in value:
                if isinstance(i, EmployeeBatchAddDTO):
                    self._employee_list.append(i)
                else:
                    self._employee_list.append(EmployeeBatchAddDTO.from_alipay_dict(i))
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_list:
            if isinstance(self.employee_list, list):
                for i in range(0, len(self.employee_list)):
                    element = self.employee_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.employee_list[i] = element.to_alipay_dict()
            if hasattr(self.employee_list, 'to_alipay_dict'):
                params['employee_list'] = self.employee_list.to_alipay_dict()
            else:
                params['employee_list'] = self.employee_list
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEmployeeBatchcreateModel()
        if 'employee_list' in d:
            o.employee_list = d['employee_list']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        return o


