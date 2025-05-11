#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceCompanyclerkQueryModel(object):

    def __init__(self):
        self._clerk_phone = None
        self._company_clerk_id = None
        self._out_clerk_id = None
        self._tax_no = None

    @property
    def clerk_phone(self):
        return self._clerk_phone

    @clerk_phone.setter
    def clerk_phone(self, value):
        self._clerk_phone = value
    @property
    def company_clerk_id(self):
        return self._company_clerk_id

    @company_clerk_id.setter
    def company_clerk_id(self, value):
        self._company_clerk_id = value
    @property
    def out_clerk_id(self):
        return self._out_clerk_id

    @out_clerk_id.setter
    def out_clerk_id(self, value):
        self._out_clerk_id = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.clerk_phone:
            if hasattr(self.clerk_phone, 'to_alipay_dict'):
                params['clerk_phone'] = self.clerk_phone.to_alipay_dict()
            else:
                params['clerk_phone'] = self.clerk_phone
        if self.company_clerk_id:
            if hasattr(self.company_clerk_id, 'to_alipay_dict'):
                params['company_clerk_id'] = self.company_clerk_id.to_alipay_dict()
            else:
                params['company_clerk_id'] = self.company_clerk_id
        if self.out_clerk_id:
            if hasattr(self.out_clerk_id, 'to_alipay_dict'):
                params['out_clerk_id'] = self.out_clerk_id.to_alipay_dict()
            else:
                params['out_clerk_id'] = self.out_clerk_id
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
        o = AlipayCommerceEcRecyclinginvoiceCompanyclerkQueryModel()
        if 'clerk_phone' in d:
            o.clerk_phone = d['clerk_phone']
        if 'company_clerk_id' in d:
            o.company_clerk_id = d['company_clerk_id']
        if 'out_clerk_id' in d:
            o.out_clerk_id = d['out_clerk_id']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


