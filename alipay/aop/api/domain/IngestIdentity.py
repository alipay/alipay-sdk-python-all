#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IngestIdentity(object):

    def __init__(self):
        self._app_code = None
        self._category = None
        self._full_business_code = None
        self._tenant_id = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def full_business_code(self):
        return self._full_business_code

    @full_business_code.setter
    def full_business_code(self, value):
        self._full_business_code = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.full_business_code:
            if hasattr(self.full_business_code, 'to_alipay_dict'):
                params['full_business_code'] = self.full_business_code.to_alipay_dict()
            else:
                params['full_business_code'] = self.full_business_code
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
        o = IngestIdentity()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'category' in d:
            o.category = d['category']
        if 'full_business_code' in d:
            o.full_business_code = d['full_business_code']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


