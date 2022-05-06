#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class InvoiceLineInfoOrder(object):

    def __init__(self):
        self._duty_free_flag = None
        self._duty_free_type = None
        self._line_amt = None
        self._measurement_unit = None
        self._product_name = None
        self._product_specification = None
        self._quantity = None
        self._tax_rate = None
        self._unit_amt = None

    @property
    def duty_free_flag(self):
        return self._duty_free_flag

    @duty_free_flag.setter
    def duty_free_flag(self, value):
        self._duty_free_flag = value
    @property
    def duty_free_type(self):
        return self._duty_free_type

    @duty_free_type.setter
    def duty_free_type(self, value):
        self._duty_free_type = value
    @property
    def line_amt(self):
        return self._line_amt

    @line_amt.setter
    def line_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._line_amt = value
        else:
            self._line_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
        if self.duty_free_flag:
            if hasattr(self.duty_free_flag, 'to_alipay_dict'):
                params['duty_free_flag'] = self.duty_free_flag.to_alipay_dict()
            else:
                params['duty_free_flag'] = self.duty_free_flag
        if self.duty_free_type:
            if hasattr(self.duty_free_type, 'to_alipay_dict'):
                params['duty_free_type'] = self.duty_free_type.to_alipay_dict()
            else:
                params['duty_free_type'] = self.duty_free_type
        if self.line_amt:
            if hasattr(self.line_amt, 'to_alipay_dict'):
                params['line_amt'] = self.line_amt.to_alipay_dict()
            else:
                params['line_amt'] = self.line_amt
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
        o = InvoiceLineInfoOrder()
        if 'duty_free_flag' in d:
            o.duty_free_flag = d['duty_free_flag']
        if 'duty_free_type' in d:
            o.duty_free_type = d['duty_free_type']
        if 'line_amt' in d:
            o.line_amt = d['line_amt']
        if 'measurement_unit' in d:
            o.measurement_unit = d['measurement_unit']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_specification' in d:
            o.product_specification = d['product_specification']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'unit_amt' in d:
            o.unit_amt = d['unit_amt']
        return o


