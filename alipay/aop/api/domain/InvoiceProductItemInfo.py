#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceProductItemInfo(object):

    def __init__(self):
        self._amount = None
        self._excluding_tax_amount = None
        self._item_name = None
        self._item_no = None
        self._original_blue_item_serial_no = None
        self._preferential_policy_flag = None
        self._price = None
        self._quantity = None
        self._row_type = None
        self._serial_no = None
        self._specification = None
        self._tax_amount = None
        self._tax_rate = None
        self._unit = None
        self._vat_special_management = None
        self._zero_rate_flag = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def excluding_tax_amount(self):
        return self._excluding_tax_amount

    @excluding_tax_amount.setter
    def excluding_tax_amount(self, value):
        self._excluding_tax_amount = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_no(self):
        return self._item_no

    @item_no.setter
    def item_no(self, value):
        self._item_no = value
    @property
    def original_blue_item_serial_no(self):
        return self._original_blue_item_serial_no

    @original_blue_item_serial_no.setter
    def original_blue_item_serial_no(self, value):
        self._original_blue_item_serial_no = value
    @property
    def preferential_policy_flag(self):
        return self._preferential_policy_flag

    @preferential_policy_flag.setter
    def preferential_policy_flag(self, value):
        self._preferential_policy_flag = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def row_type(self):
        return self._row_type

    @row_type.setter
    def row_type(self, value):
        self._row_type = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        self._specification = value
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
    @property
    def vat_special_management(self):
        return self._vat_special_management

    @vat_special_management.setter
    def vat_special_management(self, value):
        self._vat_special_management = value
    @property
    def zero_rate_flag(self):
        return self._zero_rate_flag

    @zero_rate_flag.setter
    def zero_rate_flag(self, value):
        self._zero_rate_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.excluding_tax_amount:
            if hasattr(self.excluding_tax_amount, 'to_alipay_dict'):
                params['excluding_tax_amount'] = self.excluding_tax_amount.to_alipay_dict()
            else:
                params['excluding_tax_amount'] = self.excluding_tax_amount
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_no:
            if hasattr(self.item_no, 'to_alipay_dict'):
                params['item_no'] = self.item_no.to_alipay_dict()
            else:
                params['item_no'] = self.item_no
        if self.original_blue_item_serial_no:
            if hasattr(self.original_blue_item_serial_no, 'to_alipay_dict'):
                params['original_blue_item_serial_no'] = self.original_blue_item_serial_no.to_alipay_dict()
            else:
                params['original_blue_item_serial_no'] = self.original_blue_item_serial_no
        if self.preferential_policy_flag:
            if hasattr(self.preferential_policy_flag, 'to_alipay_dict'):
                params['preferential_policy_flag'] = self.preferential_policy_flag.to_alipay_dict()
            else:
                params['preferential_policy_flag'] = self.preferential_policy_flag
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.row_type:
            if hasattr(self.row_type, 'to_alipay_dict'):
                params['row_type'] = self.row_type.to_alipay_dict()
            else:
                params['row_type'] = self.row_type
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.specification:
            if hasattr(self.specification, 'to_alipay_dict'):
                params['specification'] = self.specification.to_alipay_dict()
            else:
                params['specification'] = self.specification
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
        if self.vat_special_management:
            if hasattr(self.vat_special_management, 'to_alipay_dict'):
                params['vat_special_management'] = self.vat_special_management.to_alipay_dict()
            else:
                params['vat_special_management'] = self.vat_special_management
        if self.zero_rate_flag:
            if hasattr(self.zero_rate_flag, 'to_alipay_dict'):
                params['zero_rate_flag'] = self.zero_rate_flag.to_alipay_dict()
            else:
                params['zero_rate_flag'] = self.zero_rate_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceProductItemInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'excluding_tax_amount' in d:
            o.excluding_tax_amount = d['excluding_tax_amount']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_no' in d:
            o.item_no = d['item_no']
        if 'original_blue_item_serial_no' in d:
            o.original_blue_item_serial_no = d['original_blue_item_serial_no']
        if 'preferential_policy_flag' in d:
            o.preferential_policy_flag = d['preferential_policy_flag']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'row_type' in d:
            o.row_type = d['row_type']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'specification' in d:
            o.specification = d['specification']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'unit' in d:
            o.unit = d['unit']
        if 'vat_special_management' in d:
            o.vat_special_management = d['vat_special_management']
        if 'zero_rate_flag' in d:
            o.zero_rate_flag = d['zero_rate_flag']
        return o


