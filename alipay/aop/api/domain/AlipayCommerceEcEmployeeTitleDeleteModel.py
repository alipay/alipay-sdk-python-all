#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EmployeeTitleDTO import EmployeeTitleDTO


class AlipayCommerceEcEmployeeTitleDeleteModel(object):

    def __init__(self):
        self._employee_title_list = None

    @property
    def employee_title_list(self):
        return self._employee_title_list

    @employee_title_list.setter
    def employee_title_list(self, value):
        if isinstance(value, list):
            self._employee_title_list = list()
            for i in value:
                if isinstance(i, EmployeeTitleDTO):
                    self._employee_title_list.append(i)
                else:
                    self._employee_title_list.append(EmployeeTitleDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.employee_title_list:
            if isinstance(self.employee_title_list, list):
                for i in range(0, len(self.employee_title_list)):
                    element = self.employee_title_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.employee_title_list[i] = element.to_alipay_dict()
            if hasattr(self.employee_title_list, 'to_alipay_dict'):
                params['employee_title_list'] = self.employee_title_list.to_alipay_dict()
            else:
                params['employee_title_list'] = self.employee_title_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEmployeeTitleDeleteModel()
        if 'employee_title_list' in d:
            o.employee_title_list = d['employee_title_list']
        return o


