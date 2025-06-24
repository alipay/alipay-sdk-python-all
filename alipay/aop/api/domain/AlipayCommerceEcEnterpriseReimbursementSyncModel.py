#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReimburseInvoice import ReimburseInvoice


class AlipayCommerceEcEnterpriseReimbursementSyncModel(object):

    def __init__(self):
        self._employee_id = None
        self._enterprise_id = None
        self._invoice_list = None
        self._reimburse_status = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def invoice_list(self):
        return self._invoice_list

    @invoice_list.setter
    def invoice_list(self, value):
        if isinstance(value, list):
            self._invoice_list = list()
            for i in value:
                if isinstance(i, ReimburseInvoice):
                    self._invoice_list.append(i)
                else:
                    self._invoice_list.append(ReimburseInvoice.from_alipay_dict(i))
    @property
    def reimburse_status(self):
        return self._reimburse_status

    @reimburse_status.setter
    def reimburse_status(self, value):
        self._reimburse_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.invoice_list:
            if isinstance(self.invoice_list, list):
                for i in range(0, len(self.invoice_list)):
                    element = self.invoice_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_list, 'to_alipay_dict'):
                params['invoice_list'] = self.invoice_list.to_alipay_dict()
            else:
                params['invoice_list'] = self.invoice_list
        if self.reimburse_status:
            if hasattr(self.reimburse_status, 'to_alipay_dict'):
                params['reimburse_status'] = self.reimburse_status.to_alipay_dict()
            else:
                params['reimburse_status'] = self.reimburse_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEnterpriseReimbursementSyncModel()
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'invoice_list' in d:
            o.invoice_list = d['invoice_list']
        if 'reimburse_status' in d:
            o.reimburse_status = d['reimburse_status']
        return o


