#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class PayrcvReceiveApplyOpenApiDTO(object):

    def __init__(self):
        self._apply_amount = None
        self._apply_id = None
        self._arrangement_no = None
        self._ccy_code = None
        self._gmt_create = None
        self._inst_id = None
        self._invoiced_amt = None
        self._invoicing_amt = None
        self._sales_product_code = None
        self._sales_product_name = None
        self._settle_ip_role_id = None
        self._settle_ip_role_name = None
        self._tax_rate = None
        self._un_invoice_amt = None
        self._use_rule = None

    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._apply_amount = value
        else:
            self._apply_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def ccy_code(self):
        return self._ccy_code

    @ccy_code.setter
    def ccy_code(self, value):
        self._ccy_code = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def invoiced_amt(self):
        return self._invoiced_amt

    @invoiced_amt.setter
    def invoiced_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoiced_amt = value
        else:
            self._invoiced_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoicing_amt(self):
        return self._invoicing_amt

    @invoicing_amt.setter
    def invoicing_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoicing_amt = value
        else:
            self._invoicing_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def sales_product_code(self):
        return self._sales_product_code

    @sales_product_code.setter
    def sales_product_code(self, value):
        self._sales_product_code = value
    @property
    def sales_product_name(self):
        return self._sales_product_name

    @sales_product_name.setter
    def sales_product_name(self, value):
        self._sales_product_name = value
    @property
    def settle_ip_role_id(self):
        return self._settle_ip_role_id

    @settle_ip_role_id.setter
    def settle_ip_role_id(self, value):
        self._settle_ip_role_id = value
    @property
    def settle_ip_role_name(self):
        return self._settle_ip_role_name

    @settle_ip_role_name.setter
    def settle_ip_role_name(self, value):
        self._settle_ip_role_name = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def un_invoice_amt(self):
        return self._un_invoice_amt

    @un_invoice_amt.setter
    def un_invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._un_invoice_amt = value
        else:
            self._un_invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def use_rule(self):
        return self._use_rule

    @use_rule.setter
    def use_rule(self, value):
        self._use_rule = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.ccy_code:
            if hasattr(self.ccy_code, 'to_alipay_dict'):
                params['ccy_code'] = self.ccy_code.to_alipay_dict()
            else:
                params['ccy_code'] = self.ccy_code
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoiced_amt:
            if hasattr(self.invoiced_amt, 'to_alipay_dict'):
                params['invoiced_amt'] = self.invoiced_amt.to_alipay_dict()
            else:
                params['invoiced_amt'] = self.invoiced_amt
        if self.invoicing_amt:
            if hasattr(self.invoicing_amt, 'to_alipay_dict'):
                params['invoicing_amt'] = self.invoicing_amt.to_alipay_dict()
            else:
                params['invoicing_amt'] = self.invoicing_amt
        if self.sales_product_code:
            if hasattr(self.sales_product_code, 'to_alipay_dict'):
                params['sales_product_code'] = self.sales_product_code.to_alipay_dict()
            else:
                params['sales_product_code'] = self.sales_product_code
        if self.sales_product_name:
            if hasattr(self.sales_product_name, 'to_alipay_dict'):
                params['sales_product_name'] = self.sales_product_name.to_alipay_dict()
            else:
                params['sales_product_name'] = self.sales_product_name
        if self.settle_ip_role_id:
            if hasattr(self.settle_ip_role_id, 'to_alipay_dict'):
                params['settle_ip_role_id'] = self.settle_ip_role_id.to_alipay_dict()
            else:
                params['settle_ip_role_id'] = self.settle_ip_role_id
        if self.settle_ip_role_name:
            if hasattr(self.settle_ip_role_name, 'to_alipay_dict'):
                params['settle_ip_role_name'] = self.settle_ip_role_name.to_alipay_dict()
            else:
                params['settle_ip_role_name'] = self.settle_ip_role_name
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.un_invoice_amt:
            if hasattr(self.un_invoice_amt, 'to_alipay_dict'):
                params['un_invoice_amt'] = self.un_invoice_amt.to_alipay_dict()
            else:
                params['un_invoice_amt'] = self.un_invoice_amt
        if self.use_rule:
            if hasattr(self.use_rule, 'to_alipay_dict'):
                params['use_rule'] = self.use_rule.to_alipay_dict()
            else:
                params['use_rule'] = self.use_rule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayrcvReceiveApplyOpenApiDTO()
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'ccy_code' in d:
            o.ccy_code = d['ccy_code']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoiced_amt' in d:
            o.invoiced_amt = d['invoiced_amt']
        if 'invoicing_amt' in d:
            o.invoicing_amt = d['invoicing_amt']
        if 'sales_product_code' in d:
            o.sales_product_code = d['sales_product_code']
        if 'sales_product_name' in d:
            o.sales_product_name = d['sales_product_name']
        if 'settle_ip_role_id' in d:
            o.settle_ip_role_id = d['settle_ip_role_id']
        if 'settle_ip_role_name' in d:
            o.settle_ip_role_name = d['settle_ip_role_name']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'un_invoice_amt' in d:
            o.un_invoice_amt = d['un_invoice_amt']
        if 'use_rule' in d:
            o.use_rule = d['use_rule']
        return o


