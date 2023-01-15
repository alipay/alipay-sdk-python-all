#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class OpenApiInvoiceLineVO(object):

    def __init__(self):
        self._amt = None
        self._creator = None
        self._duty_free_flag = None
        self._duty_free_type = None
        self._gmt_create = None
        self._gmt_modified = None
        self._invoice_id = None
        self._invoice_line_id = None
        self._last_moder = None
        self._measurement_unit = None
        self._product_name = None
        self._product_name_suffix = None
        self._product_specification = None
        self._quantity = None
        self._tax_amt = None
        self._tax_classification_code = None
        self._tax_classification_short_name = None
        self._tax_exclusive_amt = None
        self._tax_rate = None
        self._tnt_inst_id = None
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
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
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
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
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
    def last_moder(self):
        return self._last_moder

    @last_moder.setter
    def last_moder(self, value):
        self._last_moder = value
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
    def product_name_suffix(self):
        return self._product_name_suffix

    @product_name_suffix.setter
    def product_name_suffix(self, value):
        self._product_name_suffix = value
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
    def tax_classification_code(self):
        return self._tax_classification_code

    @tax_classification_code.setter
    def tax_classification_code(self, value):
        self._tax_classification_code = value
    @property
    def tax_classification_short_name(self):
        return self._tax_classification_short_name

    @tax_classification_short_name.setter
    def tax_classification_short_name(self, value):
        self._tax_classification_short_name = value
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
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
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
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
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
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
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
        if self.last_moder:
            if hasattr(self.last_moder, 'to_alipay_dict'):
                params['last_moder'] = self.last_moder.to_alipay_dict()
            else:
                params['last_moder'] = self.last_moder
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
        if self.product_name_suffix:
            if hasattr(self.product_name_suffix, 'to_alipay_dict'):
                params['product_name_suffix'] = self.product_name_suffix.to_alipay_dict()
            else:
                params['product_name_suffix'] = self.product_name_suffix
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
        if self.tax_classification_code:
            if hasattr(self.tax_classification_code, 'to_alipay_dict'):
                params['tax_classification_code'] = self.tax_classification_code.to_alipay_dict()
            else:
                params['tax_classification_code'] = self.tax_classification_code
        if self.tax_classification_short_name:
            if hasattr(self.tax_classification_short_name, 'to_alipay_dict'):
                params['tax_classification_short_name'] = self.tax_classification_short_name.to_alipay_dict()
            else:
                params['tax_classification_short_name'] = self.tax_classification_short_name
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
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
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
        o = OpenApiInvoiceLineVO()
        if 'amt' in d:
            o.amt = d['amt']
        if 'creator' in d:
            o.creator = d['creator']
        if 'duty_free_flag' in d:
            o.duty_free_flag = d['duty_free_flag']
        if 'duty_free_type' in d:
            o.duty_free_type = d['duty_free_type']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_line_id' in d:
            o.invoice_line_id = d['invoice_line_id']
        if 'last_moder' in d:
            o.last_moder = d['last_moder']
        if 'measurement_unit' in d:
            o.measurement_unit = d['measurement_unit']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_name_suffix' in d:
            o.product_name_suffix = d['product_name_suffix']
        if 'product_specification' in d:
            o.product_specification = d['product_specification']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        if 'tax_classification_code' in d:
            o.tax_classification_code = d['tax_classification_code']
        if 'tax_classification_short_name' in d:
            o.tax_classification_short_name = d['tax_classification_short_name']
        if 'tax_exclusive_amt' in d:
            o.tax_exclusive_amt = d['tax_exclusive_amt']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'unit_amt' in d:
            o.unit_amt = d['unit_amt']
        return o


