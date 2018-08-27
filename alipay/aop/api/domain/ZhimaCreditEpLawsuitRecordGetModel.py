#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpLawsuitRecordGetModel(object):

    def __init__(self):
        self._company_name = None
        self._lawsuit_type = None
        self._org_no = None
        self._product_code = None
        self._transaction_id = None

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def lawsuit_type(self):
        return self._lawsuit_type

    @lawsuit_type.setter
    def lawsuit_type(self, value):
        self._lawsuit_type = value
    @property
    def org_no(self):
        return self._org_no

    @org_no.setter
    def org_no(self, value):
        self._org_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.lawsuit_type:
            if hasattr(self.lawsuit_type, 'to_alipay_dict'):
                params['lawsuit_type'] = self.lawsuit_type.to_alipay_dict()
            else:
                params['lawsuit_type'] = self.lawsuit_type
        if self.org_no:
            if hasattr(self.org_no, 'to_alipay_dict'):
                params['org_no'] = self.org_no.to_alipay_dict()
            else:
                params['org_no'] = self.org_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpLawsuitRecordGetModel()
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'lawsuit_type' in d:
            o.lawsuit_type = d['lawsuit_type']
        if 'org_no' in d:
            o.org_no = d['org_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


