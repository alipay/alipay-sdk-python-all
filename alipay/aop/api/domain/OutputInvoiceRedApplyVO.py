#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OutputInvoiceRedApplyVO(object):

    def __init__(self):
        self._blue_invoice_code = None
        self._blue_invoice_no = None
        self._invoice_material = None
        self._invoice_type = None
        self._operator = None
        self._red_amt = None
        self._red_invalid_reason_type = None
        self._red_notice_no = None
        self._red_reason = None

    @property
    def blue_invoice_code(self):
        return self._blue_invoice_code

    @blue_invoice_code.setter
    def blue_invoice_code(self, value):
        self._blue_invoice_code = value
    @property
    def blue_invoice_no(self):
        return self._blue_invoice_no

    @blue_invoice_no.setter
    def blue_invoice_no(self, value):
        self._blue_invoice_no = value
    @property
    def invoice_material(self):
        return self._invoice_material

    @invoice_material.setter
    def invoice_material(self, value):
        self._invoice_material = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def red_amt(self):
        return self._red_amt

    @red_amt.setter
    def red_amt(self, value):
        self._red_amt = value
    @property
    def red_invalid_reason_type(self):
        return self._red_invalid_reason_type

    @red_invalid_reason_type.setter
    def red_invalid_reason_type(self, value):
        self._red_invalid_reason_type = value
    @property
    def red_notice_no(self):
        return self._red_notice_no

    @red_notice_no.setter
    def red_notice_no(self, value):
        self._red_notice_no = value
    @property
    def red_reason(self):
        return self._red_reason

    @red_reason.setter
    def red_reason(self, value):
        self._red_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.blue_invoice_code:
            if hasattr(self.blue_invoice_code, 'to_alipay_dict'):
                params['blue_invoice_code'] = self.blue_invoice_code.to_alipay_dict()
            else:
                params['blue_invoice_code'] = self.blue_invoice_code
        if self.blue_invoice_no:
            if hasattr(self.blue_invoice_no, 'to_alipay_dict'):
                params['blue_invoice_no'] = self.blue_invoice_no.to_alipay_dict()
            else:
                params['blue_invoice_no'] = self.blue_invoice_no
        if self.invoice_material:
            if hasattr(self.invoice_material, 'to_alipay_dict'):
                params['invoice_material'] = self.invoice_material.to_alipay_dict()
            else:
                params['invoice_material'] = self.invoice_material
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.red_amt:
            if hasattr(self.red_amt, 'to_alipay_dict'):
                params['red_amt'] = self.red_amt.to_alipay_dict()
            else:
                params['red_amt'] = self.red_amt
        if self.red_invalid_reason_type:
            if hasattr(self.red_invalid_reason_type, 'to_alipay_dict'):
                params['red_invalid_reason_type'] = self.red_invalid_reason_type.to_alipay_dict()
            else:
                params['red_invalid_reason_type'] = self.red_invalid_reason_type
        if self.red_notice_no:
            if hasattr(self.red_notice_no, 'to_alipay_dict'):
                params['red_notice_no'] = self.red_notice_no.to_alipay_dict()
            else:
                params['red_notice_no'] = self.red_notice_no
        if self.red_reason:
            if hasattr(self.red_reason, 'to_alipay_dict'):
                params['red_reason'] = self.red_reason.to_alipay_dict()
            else:
                params['red_reason'] = self.red_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutputInvoiceRedApplyVO()
        if 'blue_invoice_code' in d:
            o.blue_invoice_code = d['blue_invoice_code']
        if 'blue_invoice_no' in d:
            o.blue_invoice_no = d['blue_invoice_no']
        if 'invoice_material' in d:
            o.invoice_material = d['invoice_material']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'operator' in d:
            o.operator = d['operator']
        if 'red_amt' in d:
            o.red_amt = d['red_amt']
        if 'red_invalid_reason_type' in d:
            o.red_invalid_reason_type = d['red_invalid_reason_type']
        if 'red_notice_no' in d:
            o.red_notice_no = d['red_notice_no']
        if 'red_reason' in d:
            o.red_reason = d['red_reason']
        return o


