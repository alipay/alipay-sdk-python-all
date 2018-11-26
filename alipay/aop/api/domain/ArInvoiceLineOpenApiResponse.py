#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class ArInvoiceLineOpenApiResponse(object):

    def __init__(self):
        self._amt = None
        self._invoice_id = None
        self._invoice_line_id = None
        self._measurement_unit = None
        self._product_name = None
        self._product_specification = None
        self._quantity = None
        self._tax_amt = None
        self._tax_exclusive_amt = None
        self._tax_rate = None
        self._unit_amt = None

    @property
    def amt(self):
        return self._amt

    @amt.setter
    def amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._amt = value
        else:
            self._amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def invoice_line_id(self):
        return self._invoice_line_id

    @invoice_line_id.setter
    def invoice_line_id(self, value):
        self._invoice_line_id = value
    @property
    def measurement_unit(self):
        return self._measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, value):
        self._measurement_unit = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_specification(self):
        return self._product_specification

    @product_specification.setter
    def product_specification(self, value):
        self._product_specification = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def tax_amt(self):
        return self._tax_amt

    @tax_amt.setter
    def tax_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._tax_amt = value
        else:
            self._tax_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def tax_exclusive_amt(self):
        return self._tax_exclusive_amt

    @tax_exclusive_amt.setter
    def tax_exclusive_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._tax_exclusive_amt = value
        else:
            self._tax_exclusive_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def unit_amt(self):
        return self._unit_amt

    @unit_amt.setter
    def unit_amt(self, value):
        self._unit_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.amt:
            if hasattr(self.amt, 'to_alipay_dict'):
                params['amt'] = self.amt.to_alipay_dict()
            else:
                params['amt'] = self.amt
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.invoice_line_id:
            if hasattr(self.invoice_line_id, 'to_alipay_dict'):
                params['invoice_line_id'] = self.invoice_line_id.to_alipay_dict()
            else:
                params['invoice_line_id'] = self.invoice_line_id
        if self.measurement_unit:
            if hasattr(self.measurement_unit, 'to_alipay_dict'):
                params['measurement_unit'] = self.measurement_unit.to_alipay_dict()
            else:
                params['measurement_unit'] = self.measurement_unit
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.product_specification:
            if hasattr(self.product_specification, 'to_alipay_dict'):
                params['product_specification'] = self.product_specification.to_alipay_dict()
            else:
                params['product_specification'] = self.product_specification
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.tax_amt:
            if hasattr(self.tax_amt, 'to_alipay_dict'):
                params['tax_amt'] = self.tax_amt.to_alipay_dict()
            else:
                params['tax_amt'] = self.tax_amt
        if self.tax_exclusive_amt:
            if hasattr(self.tax_exclusive_amt, 'to_alipay_dict'):
                params['tax_exclusive_amt'] = self.tax_exclusive_amt.to_alipay_dict()
            else:
                params['tax_exclusive_amt'] = self.tax_exclusive_amt
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.unit_amt:
            if hasattr(self.unit_amt, 'to_alipay_dict'):
                params['unit_amt'] = self.unit_amt.to_alipay_dict()
            else:
                params['unit_amt'] = self.unit_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArInvoiceLineOpenApiResponse()
        if 'amt' in d:
            o.amt = d['amt']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_line_id' in d:
            o.invoice_line_id = d['invoice_line_id']
        if 'measurement_unit' in d:
            o.measurement_unit = d['measurement_unit']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_specification' in d:
            o.product_specification = d['product_specification']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        if 'tax_exclusive_amt' in d:
            o.tax_exclusive_amt = d['tax_exclusive_amt']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'unit_amt' in d:
            o.unit_amt = d['unit_amt']
        return o


