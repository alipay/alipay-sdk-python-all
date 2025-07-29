#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcIndustryinvoiceClerkModifyModel(object):

    def __init__(self):
        self._clerk_no = None
        self._tax_no = None

    @property
    def clerk_no(self):
        return self._clerk_no

    @clerk_no.setter
    def clerk_no(self, value):
        self._clerk_no = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.clerk_no:
            if hasattr(self.clerk_no, 'to_alipay_dict'):
                params['clerk_no'] = self.clerk_no.to_alipay_dict()
            else:
                params['clerk_no'] = self.clerk_no
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
        o = AlipayCommerceEcIndustryinvoiceClerkModifyModel()
        if 'clerk_no' in d:
            o.clerk_no = d['clerk_no']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


