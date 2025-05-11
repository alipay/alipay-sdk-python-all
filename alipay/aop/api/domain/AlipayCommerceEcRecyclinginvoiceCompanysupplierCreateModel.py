#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceCompanysupplierCreateModel(object):

    def __init__(self):
        self._account_type = None
        self._outer_supplier_id = None
        self._supplier_account_no = None
        self._supplier_name = None
        self._tax_no = None

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def outer_supplier_id(self):
        return self._outer_supplier_id

    @outer_supplier_id.setter
    def outer_supplier_id(self, value):
        self._outer_supplier_id = value
    @property
    def supplier_account_no(self):
        return self._supplier_account_no

    @supplier_account_no.setter
    def supplier_account_no(self, value):
        self._supplier_account_no = value
    @property
    def supplier_name(self):
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, value):
        self._supplier_name = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.outer_supplier_id:
            if hasattr(self.outer_supplier_id, 'to_alipay_dict'):
                params['outer_supplier_id'] = self.outer_supplier_id.to_alipay_dict()
            else:
                params['outer_supplier_id'] = self.outer_supplier_id
        if self.supplier_account_no:
            if hasattr(self.supplier_account_no, 'to_alipay_dict'):
                params['supplier_account_no'] = self.supplier_account_no.to_alipay_dict()
            else:
                params['supplier_account_no'] = self.supplier_account_no
        if self.supplier_name:
            if hasattr(self.supplier_name, 'to_alipay_dict'):
                params['supplier_name'] = self.supplier_name.to_alipay_dict()
            else:
                params['supplier_name'] = self.supplier_name
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceCompanysupplierCreateModel()
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'outer_supplier_id' in d:
            o.outer_supplier_id = d['outer_supplier_id']
        if 'supplier_account_no' in d:
            o.supplier_account_no = d['supplier_account_no']
        if 'supplier_name' in d:
            o.supplier_name = d['supplier_name']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


