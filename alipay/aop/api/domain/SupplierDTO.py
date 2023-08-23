#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupplierDTO(object):

    def __init__(self):
        self._supplier_code = None
        self._supplier_id = None
        self._supplier_name = None

    @property
    def supplier_code(self):
        return self._supplier_code

    @supplier_code.setter
    def supplier_code(self, value):
        self._supplier_code = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def supplier_name(self):
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, value):
        self._supplier_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.supplier_code:
            if hasattr(self.supplier_code, 'to_alipay_dict'):
                params['supplier_code'] = self.supplier_code.to_alipay_dict()
            else:
                params['supplier_code'] = self.supplier_code
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.supplier_name:
            if hasattr(self.supplier_name, 'to_alipay_dict'):
                params['supplier_name'] = self.supplier_name.to_alipay_dict()
            else:
                params['supplier_name'] = self.supplier_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupplierDTO()
        if 'supplier_code' in d:
            o.supplier_code = d['supplier_code']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'supplier_name' in d:
            o.supplier_name = d['supplier_name']
        return o


