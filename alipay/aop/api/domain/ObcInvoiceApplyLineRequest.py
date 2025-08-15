#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ObcInvoiceObjectRequest import ObcInvoiceObjectRequest


class ObcInvoiceApplyLineRequest(object):

    def __init__(self):
        self._currency_code = None
        self._details = None
        self._invoice_amount = None
        self._invoice_specification = None
        self._price = None
        self._product_name = None
        self._quantity = None
        self._tax_amount = None
        self._tax_rate = None
        self._unit = None

    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value
    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if isinstance(value, list):
            self._details = list()
            for i in value:
                if isinstance(i, ObcInvoiceObjectRequest):
                    self._details.append(i)
                else:
                    self._details.append(ObcInvoiceObjectRequest.from_alipay_dict(i))
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def invoice_specification(self):
        return self._invoice_specification

    @invoice_specification.setter
    def invoice_specification(self, value):
        self._invoice_specification = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        if self.details:
            if isinstance(self.details, list):
                for i in range(0, len(self.details)):
                    element = self.details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.details[i] = element.to_alipay_dict()
            if hasattr(self.details, 'to_alipay_dict'):
                params['details'] = self.details.to_alipay_dict()
            else:
                params['details'] = self.details
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.invoice_specification:
            if hasattr(self.invoice_specification, 'to_alipay_dict'):
                params['invoice_specification'] = self.invoice_specification.to_alipay_dict()
            else:
                params['invoice_specification'] = self.invoice_specification
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObcInvoiceApplyLineRequest()
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'details' in d:
            o.details = d['details']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_specification' in d:
            o.invoice_specification = d['invoice_specification']
        if 'price' in d:
            o.price = d['price']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'unit' in d:
            o.unit = d['unit']
        return o


