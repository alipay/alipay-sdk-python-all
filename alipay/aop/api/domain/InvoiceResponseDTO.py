#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class InvoiceResponseDTO(object):

    def __init__(self):
        self._exclude_tax_invoice_amt = None
        self._invoice_amt = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_id = None
        self._invoice_no = None
        self._invoice_rcv_date = None
        self._invoice_status = None
        self._invoice_type = None
        self._invoice_type_name = None
        self._tax_amt = None
        self._tax_rate = None

    @property
    def exclude_tax_invoice_amt(self):
        return self._exclude_tax_invoice_amt

    @exclude_tax_invoice_amt.setter
    def exclude_tax_invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._exclude_tax_invoice_amt = value
        else:
            self._exclude_tax_invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoice_amt(self):
        return self._invoice_amt

    @invoice_amt.setter
    def invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoice_amt = value
        else:
            self._invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_rcv_date(self):
        return self._invoice_rcv_date

    @invoice_rcv_date.setter
    def invoice_rcv_date(self, value):
        self._invoice_rcv_date = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def invoice_type_name(self):
        return self._invoice_type_name

    @invoice_type_name.setter
    def invoice_type_name(self, value):
        self._invoice_type_name = value
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
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.exclude_tax_invoice_amt:
            if hasattr(self.exclude_tax_invoice_amt, 'to_alipay_dict'):
                params['exclude_tax_invoice_amt'] = self.exclude_tax_invoice_amt.to_alipay_dict()
            else:
                params['exclude_tax_invoice_amt'] = self.exclude_tax_invoice_amt
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_rcv_date:
            if hasattr(self.invoice_rcv_date, 'to_alipay_dict'):
                params['invoice_rcv_date'] = self.invoice_rcv_date.to_alipay_dict()
            else:
                params['invoice_rcv_date'] = self.invoice_rcv_date
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.invoice_type_name:
            if hasattr(self.invoice_type_name, 'to_alipay_dict'):
                params['invoice_type_name'] = self.invoice_type_name.to_alipay_dict()
            else:
                params['invoice_type_name'] = self.invoice_type_name
        if self.tax_amt:
            if hasattr(self.tax_amt, 'to_alipay_dict'):
                params['tax_amt'] = self.tax_amt.to_alipay_dict()
            else:
                params['tax_amt'] = self.tax_amt
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceResponseDTO()
        if 'exclude_tax_invoice_amt' in d:
            o.exclude_tax_invoice_amt = d['exclude_tax_invoice_amt']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_rcv_date' in d:
            o.invoice_rcv_date = d['invoice_rcv_date']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'invoice_type_name' in d:
            o.invoice_type_name = d['invoice_type_name']
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


