#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpRebusinessentityStoreQueryModel(object):

    def __init__(self):
        self._platform_id = None
        self._platform_id_list = None
        self._platform_type_list = None
        self._product_code = None
        self._rel_type_code_list = None
        self._store_id = None

    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value
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
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
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
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpRebusinessentityStoreQueryModel()
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        if 'platform_id_list' in d:
            o.platform_id_list = d['platform_id_list']
        if 'platform_type_list' in d:
            o.platform_type_list = d['platform_type_list']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'rel_type_code_list' in d:
            o.rel_type_code_list = d['rel_type_code_list']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


