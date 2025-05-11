#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupplierQueryOpenResult(object):

    def __init__(self):
        self._account_type = None
        self._supplier_account_no = None
        self._supplier_name = None
        self._supplier_phone = None

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
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
    def supplier_phone(self):
        return self._supplier_phone

    @supplier_phone.setter
    def supplier_phone(self, value):
        self._supplier_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
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
        if self.supplier_phone:
            if hasattr(self.supplier_phone, 'to_alipay_dict'):
                params['supplier_phone'] = self.supplier_phone.to_alipay_dict()
            else:
                params['supplier_phone'] = self.supplier_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupplierQueryOpenResult()
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'supplier_account_no' in d:
            o.supplier_account_no = d['supplier_account_no']
        if 'supplier_name' in d:
            o.supplier_name = d['supplier_name']
        if 'supplier_phone' in d:
            o.supplier_phone = d['supplier_phone']
        return o


