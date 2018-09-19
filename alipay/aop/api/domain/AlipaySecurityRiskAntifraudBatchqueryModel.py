#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskAntifraudBatchqueryModel(object):

    def __init__(self):
        self._company_list = None
        self._partner_name = None
        self._staff_list = None

    @property
    def company_list(self):
        return self._company_list

    @company_list.setter
    def company_list(self, value):
        if isinstance(value, list):
            self._company_list = list()
            for i in value:
                self._company_list.append(i)
    @property
    def partner_name(self):
        return self._partner_name

    @partner_name.setter
    def partner_name(self, value):
        self._partner_name = value
    @property
    def staff_list(self):
        return self._staff_list

    @staff_list.setter
    def staff_list(self, value):
        if isinstance(value, list):
            self._staff_list = list()
            for i in value:
                self._staff_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.company_list:
            if isinstance(self.company_list, list):
                for i in range(0, len(self.company_list)):
                    element = self.company_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.company_list[i] = element.to_alipay_dict()
            if hasattr(self.company_list, 'to_alipay_dict'):
                params['company_list'] = self.company_list.to_alipay_dict()
            else:
                params['company_list'] = self.company_list
        if self.partner_name:
            if hasattr(self.partner_name, 'to_alipay_dict'):
                params['partner_name'] = self.partner_name.to_alipay_dict()
            else:
                params['partner_name'] = self.partner_name
        if self.staff_list:
            if isinstance(self.staff_list, list):
                for i in range(0, len(self.staff_list)):
                    element = self.staff_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.staff_list[i] = element.to_alipay_dict()
            if hasattr(self.staff_list, 'to_alipay_dict'):
                params['staff_list'] = self.staff_list.to_alipay_dict()
            else:
                params['staff_list'] = self.staff_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskAntifraudBatchqueryModel()
        if 'company_list' in d:
            o.company_list = d['company_list']
        if 'partner_name' in d:
            o.partner_name = d['partner_name']
        if 'staff_list' in d:
            o.staff_list = d['staff_list']
        return o


