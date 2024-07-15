#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpRebusinessentityCompanyQueryModel(object):

    def __init__(self):
        self._company_key = None
        self._platform_id_list = None
        self._platform_type_list = None
        self._product_code = None
        self._rel_type_code_list = None

    @property
    def company_key(self):
        return self._company_key

    @company_key.setter
    def company_key(self, value):
        self._company_key = value
    @property
    def platform_id_list(self):
        return self._platform_id_list

    @platform_id_list.setter
    def platform_id_list(self, value):
        if isinstance(value, list):
            self._platform_id_list = list()
            for i in value:
                self._platform_id_list.append(i)
    @property
    def platform_type_list(self):
        return self._platform_type_list

    @platform_type_list.setter
    def platform_type_list(self, value):
        if isinstance(value, list):
            self._platform_type_list = list()
            for i in value:
                self._platform_type_list.append(i)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def rel_type_code_list(self):
        return self._rel_type_code_list

    @rel_type_code_list.setter
    def rel_type_code_list(self, value):
        if isinstance(value, list):
            self._rel_type_code_list = list()
            for i in value:
                self._rel_type_code_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.company_key:
            if hasattr(self.company_key, 'to_alipay_dict'):
                params['company_key'] = self.company_key.to_alipay_dict()
            else:
                params['company_key'] = self.company_key
        if self.platform_id_list:
            if isinstance(self.platform_id_list, list):
                for i in range(0, len(self.platform_id_list)):
                    element = self.platform_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.platform_id_list[i] = element.to_alipay_dict()
            if hasattr(self.platform_id_list, 'to_alipay_dict'):
                params['platform_id_list'] = self.platform_id_list.to_alipay_dict()
            else:
                params['platform_id_list'] = self.platform_id_list
        if self.platform_type_list:
            if isinstance(self.platform_type_list, list):
                for i in range(0, len(self.platform_type_list)):
                    element = self.platform_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.platform_type_list[i] = element.to_alipay_dict()
            if hasattr(self.platform_type_list, 'to_alipay_dict'):
                params['platform_type_list'] = self.platform_type_list.to_alipay_dict()
            else:
                params['platform_type_list'] = self.platform_type_list
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.rel_type_code_list:
            if isinstance(self.rel_type_code_list, list):
                for i in range(0, len(self.rel_type_code_list)):
                    element = self.rel_type_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rel_type_code_list[i] = element.to_alipay_dict()
            if hasattr(self.rel_type_code_list, 'to_alipay_dict'):
                params['rel_type_code_list'] = self.rel_type_code_list.to_alipay_dict()
            else:
                params['rel_type_code_list'] = self.rel_type_code_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpRebusinessentityCompanyQueryModel()
        if 'company_key' in d:
            o.company_key = d['company_key']
        if 'platform_id_list' in d:
            o.platform_id_list = d['platform_id_list']
        if 'platform_type_list' in d:
            o.platform_type_list = d['platform_type_list']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'rel_type_code_list' in d:
            o.rel_type_code_list = d['rel_type_code_list']
        return o


