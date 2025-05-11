#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceCompanyaccountQueryModel(object):

    def __init__(self):
        self._company_account_id = None
        self._tax_no = None

    @property
    def company_account_id(self):
        return self._company_account_id

    @company_account_id.setter
    def company_account_id(self, value):
        self._company_account_id = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_account_id:
            if hasattr(self.company_account_id, 'to_alipay_dict'):
                params['company_account_id'] = self.company_account_id.to_alipay_dict()
            else:
                params['company_account_id'] = self.company_account_id
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
        o = AlipayCommerceEcRecyclinginvoiceCompanyaccountQueryModel()
        if 'company_account_id' in d:
            o.company_account_id = d['company_account_id']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


