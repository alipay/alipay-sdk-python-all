#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CompanyProductConfig import CompanyProductConfig


class CompanyProduct(object):

    def __init__(self):
        self._company_account_id = None
        self._company_product_config = None
        self._product_id = None
        self._product_name = None

    @property
    def company_account_id(self):
        return self._company_account_id

    @company_account_id.setter
    def company_account_id(self, value):
        self._company_account_id = value
    @property
    def company_product_config(self):
        return self._company_product_config

    @company_product_config.setter
    def company_product_config(self, value):
        if isinstance(value, CompanyProductConfig):
            self._company_product_config = value
        else:
            self._company_product_config = CompanyProductConfig.from_alipay_dict(value)
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_account_id:
            if hasattr(self.company_account_id, 'to_alipay_dict'):
                params['company_account_id'] = self.company_account_id.to_alipay_dict()
            else:
                params['company_account_id'] = self.company_account_id
        if self.company_product_config:
            if hasattr(self.company_product_config, 'to_alipay_dict'):
                params['company_product_config'] = self.company_product_config.to_alipay_dict()
            else:
                params['company_product_config'] = self.company_product_config
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyProduct()
        if 'company_account_id' in d:
            o.company_account_id = d['company_account_id']
        if 'company_product_config' in d:
            o.company_product_config = d['company_product_config']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_name' in d:
            o.product_name = d['product_name']
        return o


