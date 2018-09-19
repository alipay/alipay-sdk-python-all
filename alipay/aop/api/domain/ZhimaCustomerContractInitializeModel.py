#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerContractInitializeModel(object):

    def __init__(self):
        self._contract_file = None
        self._contract_name = None
        self._product_code = None

    @property
    def contract_file(self):
        return self._contract_file

    @contract_file.setter
    def contract_file(self, value):
        self._contract_file = value
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_file:
            if hasattr(self.contract_file, 'to_alipay_dict'):
                params['contract_file'] = self.contract_file.to_alipay_dict()
            else:
                params['contract_file'] = self.contract_file
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerContractInitializeModel()
        if 'contract_file' in d:
            o.contract_file = d['contract_file']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


