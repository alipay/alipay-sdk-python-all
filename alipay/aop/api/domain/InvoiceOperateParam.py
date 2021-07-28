#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceOperateParam(object):

    def __init__(self):
        self._invoice_id = None
        self._operator = None
        self._operator_type = None

    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceOperateParam()
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        return o


