#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryInvoiceItemInfoQueryRes(object):

    def __init__(self):
        self._favoured_policy_flag = None
        self._invoice_line_property = None
        self._item_amount = None
        self._item_category_name = None
        self._item_code = None
        self._item_name = None
        self._item_num = None
        self._item_spec = None
        self._item_tax_amount = None
        self._item_tax_rate = None
        self._item_unit = None
        self._related_blue_serial_no = None
        self._serial_no = None
        self._tax_code = None

    @property
    def favoured_policy_flag(self):
        return self._favoured_policy_flag

    @favoured_policy_flag.setter
    def favoured_policy_flag(self, value):
        self._favoured_policy_flag = value
    @property
    def invoice_line_property(self):
        return self._invoice_line_property

    @invoice_line_property.setter
    def invoice_line_property(self, value):
        self._invoice_line_property = value
    @property
    def item_amount(self):
        return self._item_amount

    @item_amount.setter
    def item_amount(self, value):
        self._item_amount = value
    @property
    def item_category_name(self):
        return self._item_category_name

    @item_category_name.setter
    def item_category_name(self, value):
        self._item_category_name = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_num(self):
        return self._item_num

    @item_num.setter
    def item_num(self, value):
        self._item_num = value
    @property
    def item_spec(self):
        return self._item_spec

    @item_spec.setter
    def item_spec(self, value):
        self._item_spec = value
    @property
    def item_tax_amount(self):
        return self._item_tax_amount

    @item_tax_amount.setter
    def item_tax_amount(self, value):
        self._item_tax_amount = value
    @property
    def item_tax_rate(self):
        return self._item_tax_rate

    @item_tax_rate.setter
    def item_tax_rate(self, value):
        self._item_tax_rate = value
    @property
    def item_unit(self):
        return self._item_unit

    @item_unit.setter
    def item_unit(self, value):
        self._item_unit = value
    @property
    def related_blue_serial_no(self):
        return self._related_blue_serial_no

    @related_blue_serial_no.setter
    def related_blue_serial_no(self, value):
        self._related_blue_serial_no = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def tax_code(self):
        return self._tax_code

    @tax_code.setter
    def tax_code(self, value):
        self._tax_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.favoured_policy_flag:
            if hasattr(self.favoured_policy_flag, 'to_alipay_dict'):
                params['favoured_policy_flag'] = self.favoured_policy_flag.to_alipay_dict()
            else:
                params['favoured_policy_flag'] = self.favoured_policy_flag
        if self.invoice_line_property:
            if hasattr(self.invoice_line_property, 'to_alipay_dict'):
                params['invoice_line_property'] = self.invoice_line_property.to_alipay_dict()
            else:
                params['invoice_line_property'] = self.invoice_line_property
        if self.item_amount:
            if hasattr(self.item_amount, 'to_alipay_dict'):
                params['item_amount'] = self.item_amount.to_alipay_dict()
            else:
                params['item_amount'] = self.item_amount
        if self.item_category_name:
            if hasattr(self.item_category_name, 'to_alipay_dict'):
                params['item_category_name'] = self.item_category_name.to_alipay_dict()
            else:
                params['item_category_name'] = self.item_category_name
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_num:
            if hasattr(self.item_num, 'to_alipay_dict'):
                params['item_num'] = self.item_num.to_alipay_dict()
            else:
                params['item_num'] = self.item_num
        if self.item_spec:
            if hasattr(self.item_spec, 'to_alipay_dict'):
                params['item_spec'] = self.item_spec.to_alipay_dict()
            else:
                params['item_spec'] = self.item_spec
        if self.item_tax_amount:
            if hasattr(self.item_tax_amount, 'to_alipay_dict'):
                params['item_tax_amount'] = self.item_tax_amount.to_alipay_dict()
            else:
                params['item_tax_amount'] = self.item_tax_amount
        if self.item_tax_rate:
            if hasattr(self.item_tax_rate, 'to_alipay_dict'):
                params['item_tax_rate'] = self.item_tax_rate.to_alipay_dict()
            else:
                params['item_tax_rate'] = self.item_tax_rate
        if self.item_unit:
            if hasattr(self.item_unit, 'to_alipay_dict'):
                params['item_unit'] = self.item_unit.to_alipay_dict()
            else:
                params['item_unit'] = self.item_unit
        if self.related_blue_serial_no:
            if hasattr(self.related_blue_serial_no, 'to_alipay_dict'):
                params['related_blue_serial_no'] = self.related_blue_serial_no.to_alipay_dict()
            else:
                params['related_blue_serial_no'] = self.related_blue_serial_no
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.tax_code:
            if hasattr(self.tax_code, 'to_alipay_dict'):
                params['tax_code'] = self.tax_code.to_alipay_dict()
            else:
                params['tax_code'] = self.tax_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryInvoiceItemInfoQueryRes()
        if 'favoured_policy_flag' in d:
            o.favoured_policy_flag = d['favoured_policy_flag']
        if 'invoice_line_property' in d:
            o.invoice_line_property = d['invoice_line_property']
        if 'item_amount' in d:
            o.item_amount = d['item_amount']
        if 'item_category_name' in d:
            o.item_category_name = d['item_category_name']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_num' in d:
            o.item_num = d['item_num']
        if 'item_spec' in d:
            o.item_spec = d['item_spec']
        if 'item_tax_amount' in d:
            o.item_tax_amount = d['item_tax_amount']
        if 'item_tax_rate' in d:
            o.item_tax_rate = d['item_tax_rate']
        if 'item_unit' in d:
            o.item_unit = d['item_unit']
        if 'related_blue_serial_no' in d:
            o.related_blue_serial_no = d['related_blue_serial_no']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'tax_code' in d:
            o.tax_code = d['tax_code']
        return o


