#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class InvoiceApplyOpenApi(object):

    def __init__(self):
        self._amount = None
        self._arrangement_no = None
        self._duty_free_type = None
        self._inst_id = None
        self._invoice_date = None
        self._invoice_product_name = None
        self._invoice_specification = None
        self._ip_id = None
        self._ip_role_id = None
        self._out_biz_no = None
        self._out_biz_type = None
        self._product_code = None
        self._service_mth = None
        self._tax_rate = None
        self._tax_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._amount = value
        else:
            self._amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def duty_free_type(self):
        return self._duty_free_type

    @duty_free_type.setter
    def duty_free_type(self, value):
        self._duty_free_type = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_product_name(self):
        return self._invoice_product_name

    @invoice_product_name.setter
    def invoice_product_name(self, value):
        self._invoice_product_name = value
    @property
    def invoice_specification(self):
        return self._invoice_specification

    @invoice_specification.setter
    def invoice_specification(self, value):
        self._invoice_specification = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def service_mth(self):
        return self._service_mth

    @service_mth.setter
    def service_mth(self, value):
        self._service_mth = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, value):
        self._tax_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.duty_free_type:
            if hasattr(self.duty_free_type, 'to_alipay_dict'):
                params['duty_free_type'] = self.duty_free_type.to_alipay_dict()
            else:
                params['duty_free_type'] = self.duty_free_type
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_product_name:
            if hasattr(self.invoice_product_name, 'to_alipay_dict'):
                params['invoice_product_name'] = self.invoice_product_name.to_alipay_dict()
            else:
                params['invoice_product_name'] = self.invoice_product_name
        if self.invoice_specification:
            if hasattr(self.invoice_specification, 'to_alipay_dict'):
                params['invoice_specification'] = self.invoice_specification.to_alipay_dict()
            else:
                params['invoice_specification'] = self.invoice_specification
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.service_mth:
            if hasattr(self.service_mth, 'to_alipay_dict'):
                params['service_mth'] = self.service_mth.to_alipay_dict()
            else:
                params['service_mth'] = self.service_mth
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.tax_type:
            if hasattr(self.tax_type, 'to_alipay_dict'):
                params['tax_type'] = self.tax_type.to_alipay_dict()
            else:
                params['tax_type'] = self.tax_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceApplyOpenApi()
        if 'amount' in d:
            o.amount = d['amount']
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'duty_free_type' in d:
            o.duty_free_type = d['duty_free_type']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_product_name' in d:
            o.invoice_product_name = d['invoice_product_name']
        if 'invoice_specification' in d:
            o.invoice_specification = d['invoice_specification']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'service_mth' in d:
            o.service_mth = d['service_mth']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tax_type' in d:
            o.tax_type = d['tax_type']
        return o


