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
        self._fee_interval_format_str = None
        self._inst_id = None
        self._inv_dt = None
        self._invoice_date = None
        self._invoice_line_measurement_unit = None
        self._invoice_line_quantity = None
        self._invoice_line_unit_amount = None
        self._invoice_note = None
        self._invoice_product_name = None
        self._invoice_product_name_suffix = None
        self._invoice_specification = None
        self._invoice_split_key = None
        self._invoice_type = None
        self._ip_id = None
        self._ip_role_id = None
        self._out_biz_no = None
        self._out_biz_type = None
        self._product_code = None
        self._received = None
        self._register_country = None
        self._service_mth = None
        self._source = None
        self._tax_classification_code = None
        self._tax_rate = None
        self._tax_rate_tags = None
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
    def fee_interval_format_str(self):
        return self._fee_interval_format_str

    @fee_interval_format_str.setter
    def fee_interval_format_str(self, value):
        self._fee_interval_format_str = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inv_dt(self):
        return self._inv_dt

    @inv_dt.setter
    def inv_dt(self, value):
        self._inv_dt = value
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_line_measurement_unit(self):
        return self._invoice_line_measurement_unit

    @invoice_line_measurement_unit.setter
    def invoice_line_measurement_unit(self, value):
        self._invoice_line_measurement_unit = value
    @property
    def invoice_line_quantity(self):
        return self._invoice_line_quantity

    @invoice_line_quantity.setter
    def invoice_line_quantity(self, value):
        self._invoice_line_quantity = value
    @property
    def invoice_line_unit_amount(self):
        return self._invoice_line_unit_amount

    @invoice_line_unit_amount.setter
    def invoice_line_unit_amount(self, value):
        self._invoice_line_unit_amount = value
    @property
    def invoice_note(self):
        return self._invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self._invoice_note = value
    @property
    def invoice_product_name(self):
        return self._invoice_product_name

    @invoice_product_name.setter
    def invoice_product_name(self, value):
        self._invoice_product_name = value
    @property
    def invoice_product_name_suffix(self):
        return self._invoice_product_name_suffix

    @invoice_product_name_suffix.setter
    def invoice_product_name_suffix(self, value):
        self._invoice_product_name_suffix = value
    @property
    def invoice_specification(self):
        return self._invoice_specification

    @invoice_specification.setter
    def invoice_specification(self, value):
        self._invoice_specification = value
    @property
    def invoice_split_key(self):
        return self._invoice_split_key

    @invoice_split_key.setter
    def invoice_split_key(self, value):
        self._invoice_split_key = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
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
    def received(self):
        return self._received

    @received.setter
    def received(self, value):
        self._received = value
    @property
    def register_country(self):
        return self._register_country

    @register_country.setter
    def register_country(self, value):
        self._register_country = value
    @property
    def service_mth(self):
        return self._service_mth

    @service_mth.setter
    def service_mth(self, value):
        self._service_mth = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def tax_classification_code(self):
        return self._tax_classification_code

    @tax_classification_code.setter
    def tax_classification_code(self, value):
        self._tax_classification_code = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def tax_rate_tags(self):
        return self._tax_rate_tags

    @tax_rate_tags.setter
    def tax_rate_tags(self, value):
        self._tax_rate_tags = value
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
        if self.fee_interval_format_str:
            if hasattr(self.fee_interval_format_str, 'to_alipay_dict'):
                params['fee_interval_format_str'] = self.fee_interval_format_str.to_alipay_dict()
            else:
                params['fee_interval_format_str'] = self.fee_interval_format_str
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inv_dt:
            if hasattr(self.inv_dt, 'to_alipay_dict'):
                params['inv_dt'] = self.inv_dt.to_alipay_dict()
            else:
                params['inv_dt'] = self.inv_dt
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_line_measurement_unit:
            if hasattr(self.invoice_line_measurement_unit, 'to_alipay_dict'):
                params['invoice_line_measurement_unit'] = self.invoice_line_measurement_unit.to_alipay_dict()
            else:
                params['invoice_line_measurement_unit'] = self.invoice_line_measurement_unit
        if self.invoice_line_quantity:
            if hasattr(self.invoice_line_quantity, 'to_alipay_dict'):
                params['invoice_line_quantity'] = self.invoice_line_quantity.to_alipay_dict()
            else:
                params['invoice_line_quantity'] = self.invoice_line_quantity
        if self.invoice_line_unit_amount:
            if hasattr(self.invoice_line_unit_amount, 'to_alipay_dict'):
                params['invoice_line_unit_amount'] = self.invoice_line_unit_amount.to_alipay_dict()
            else:
                params['invoice_line_unit_amount'] = self.invoice_line_unit_amount
        if self.invoice_note:
            if hasattr(self.invoice_note, 'to_alipay_dict'):
                params['invoice_note'] = self.invoice_note.to_alipay_dict()
            else:
                params['invoice_note'] = self.invoice_note
        if self.invoice_product_name:
            if hasattr(self.invoice_product_name, 'to_alipay_dict'):
                params['invoice_product_name'] = self.invoice_product_name.to_alipay_dict()
            else:
                params['invoice_product_name'] = self.invoice_product_name
        if self.invoice_product_name_suffix:
            if hasattr(self.invoice_product_name_suffix, 'to_alipay_dict'):
                params['invoice_product_name_suffix'] = self.invoice_product_name_suffix.to_alipay_dict()
            else:
                params['invoice_product_name_suffix'] = self.invoice_product_name_suffix
        if self.invoice_specification:
            if hasattr(self.invoice_specification, 'to_alipay_dict'):
                params['invoice_specification'] = self.invoice_specification.to_alipay_dict()
            else:
                params['invoice_specification'] = self.invoice_specification
        if self.invoice_split_key:
            if hasattr(self.invoice_split_key, 'to_alipay_dict'):
                params['invoice_split_key'] = self.invoice_split_key.to_alipay_dict()
            else:
                params['invoice_split_key'] = self.invoice_split_key
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
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
        if self.received:
            if hasattr(self.received, 'to_alipay_dict'):
                params['received'] = self.received.to_alipay_dict()
            else:
                params['received'] = self.received
        if self.register_country:
            if hasattr(self.register_country, 'to_alipay_dict'):
                params['register_country'] = self.register_country.to_alipay_dict()
            else:
                params['register_country'] = self.register_country
        if self.service_mth:
            if hasattr(self.service_mth, 'to_alipay_dict'):
                params['service_mth'] = self.service_mth.to_alipay_dict()
            else:
                params['service_mth'] = self.service_mth
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.tax_classification_code:
            if hasattr(self.tax_classification_code, 'to_alipay_dict'):
                params['tax_classification_code'] = self.tax_classification_code.to_alipay_dict()
            else:
                params['tax_classification_code'] = self.tax_classification_code
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.tax_rate_tags:
            if hasattr(self.tax_rate_tags, 'to_alipay_dict'):
                params['tax_rate_tags'] = self.tax_rate_tags.to_alipay_dict()
            else:
                params['tax_rate_tags'] = self.tax_rate_tags
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
        if 'fee_interval_format_str' in d:
            o.fee_interval_format_str = d['fee_interval_format_str']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inv_dt' in d:
            o.inv_dt = d['inv_dt']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_line_measurement_unit' in d:
            o.invoice_line_measurement_unit = d['invoice_line_measurement_unit']
        if 'invoice_line_quantity' in d:
            o.invoice_line_quantity = d['invoice_line_quantity']
        if 'invoice_line_unit_amount' in d:
            o.invoice_line_unit_amount = d['invoice_line_unit_amount']
        if 'invoice_note' in d:
            o.invoice_note = d['invoice_note']
        if 'invoice_product_name' in d:
            o.invoice_product_name = d['invoice_product_name']
        if 'invoice_product_name_suffix' in d:
            o.invoice_product_name_suffix = d['invoice_product_name_suffix']
        if 'invoice_specification' in d:
            o.invoice_specification = d['invoice_specification']
        if 'invoice_split_key' in d:
            o.invoice_split_key = d['invoice_split_key']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
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
        if 'received' in d:
            o.received = d['received']
        if 'register_country' in d:
            o.register_country = d['register_country']
        if 'service_mth' in d:
            o.service_mth = d['service_mth']
        if 'source' in d:
            o.source = d['source']
        if 'tax_classification_code' in d:
            o.tax_classification_code = d['tax_classification_code']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tax_rate_tags' in d:
            o.tax_rate_tags = d['tax_rate_tags']
        if 'tax_type' in d:
            o.tax_type = d['tax_type']
        return o


