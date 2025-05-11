#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CompanyProductConfig import CompanyProductConfig


class AlipayCommerceEcRecyclinginvoiceCompanyproductModifyModel(object):

    def __init__(self):
        self._product_config = None
        self._product_id = None
        self._tax_no = None

    @property
    def product_config(self):
        return self._product_config

    @product_config.setter
    def product_config(self, value):
        if isinstance(value, CompanyProductConfig):
            self._product_config = value
        else:
            self._product_config = CompanyProductConfig.from_alipay_dict(value)
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_config:
            if hasattr(self.product_config, 'to_alipay_dict'):
                params['product_config'] = self.product_config.to_alipay_dict()
            else:
                params['product_config'] = self.product_config
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
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
        o = AlipayCommerceEcRecyclinginvoiceCompanyproductModifyModel()
        if 'product_config' in d:
            o.product_config = d['product_config']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


