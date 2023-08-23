#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaxInfoDto(object):

    def __init__(self):
        self._address = None
        self._bank_name = None
        self._effective_date = None
        self._invoice_title = None
        self._org_id = None
        self._phone_no = None
        self._tax_no = None
        self._type = None
        self._type_desc = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
    @property
    def invoice_title(self):
        return self._invoice_title

    @invoice_title.setter
    def invoice_title(self, value):
        self._invoice_title = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def type_desc(self):
        return self._type_desc

    @type_desc.setter
    def type_desc(self, value):
        self._type_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.effective_date:
            if hasattr(self.effective_date, 'to_alipay_dict'):
                params['effective_date'] = self.effective_date.to_alipay_dict()
            else:
                params['effective_date'] = self.effective_date
        if self.invoice_title:
            if hasattr(self.invoice_title, 'to_alipay_dict'):
                params['invoice_title'] = self.invoice_title.to_alipay_dict()
            else:
                params['invoice_title'] = self.invoice_title
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.type_desc:
            if hasattr(self.type_desc, 'to_alipay_dict'):
                params['type_desc'] = self.type_desc.to_alipay_dict()
            else:
                params['type_desc'] = self.type_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaxInfoDto()
        if 'address' in d:
            o.address = d['address']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'invoice_title' in d:
            o.invoice_title = d['invoice_title']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'type' in d:
            o.type = d['type']
        if 'type_desc' in d:
            o.type_desc = d['type_desc']
        return o


