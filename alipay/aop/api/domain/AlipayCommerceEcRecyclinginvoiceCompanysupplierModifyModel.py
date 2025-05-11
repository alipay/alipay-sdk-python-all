#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceCompanysupplierModifyModel(object):

    def __init__(self):
        self._supplier_id = None
        self._supplier_phone = None
        self._tax_no = None

    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def supplier_phone(self):
        return self._supplier_phone

    @supplier_phone.setter
    def supplier_phone(self, value):
        self._supplier_phone = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.supplier_phone:
            if hasattr(self.supplier_phone, 'to_alipay_dict'):
                params['supplier_phone'] = self.supplier_phone.to_alipay_dict()
            else:
                params['supplier_phone'] = self.supplier_phone
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
        o = AlipayCommerceEcRecyclinginvoiceCompanysupplierModifyModel()
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'supplier_phone' in d:
            o.supplier_phone = d['supplier_phone']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


