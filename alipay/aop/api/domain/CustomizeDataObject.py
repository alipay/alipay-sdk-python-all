#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomizeDataObject(object):

    def __init__(self):
        self._instance_id = None
        self._product_code = None
        self._tenant_company_name = None
        self._tenant_id = None

    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def tenant_company_name(self):
        return self._tenant_company_name

    @tenant_company_name.setter
    def tenant_company_name(self, value):
        self._tenant_company_name = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.tenant_company_name:
            if hasattr(self.tenant_company_name, 'to_alipay_dict'):
                params['tenant_company_name'] = self.tenant_company_name.to_alipay_dict()
            else:
                params['tenant_company_name'] = self.tenant_company_name
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomizeDataObject()
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'tenant_company_name' in d:
            o.tenant_company_name = d['tenant_company_name']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


