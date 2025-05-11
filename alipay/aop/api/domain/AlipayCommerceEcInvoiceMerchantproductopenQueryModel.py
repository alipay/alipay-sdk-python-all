#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcInvoiceMerchantproductopenQueryModel(object):

    def __init__(self):
        self._apply_id = None
        self._out_apply_id = None
        self._tax_no = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def out_apply_id(self):
        return self._out_apply_id

    @out_apply_id.setter
    def out_apply_id(self, value):
        self._out_apply_id = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.out_apply_id:
            if hasattr(self.out_apply_id, 'to_alipay_dict'):
                params['out_apply_id'] = self.out_apply_id.to_alipay_dict()
            else:
                params['out_apply_id'] = self.out_apply_id
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
        o = AlipayCommerceEcInvoiceMerchantproductopenQueryModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'out_apply_id' in d:
            o.out_apply_id = d['out_apply_id']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


