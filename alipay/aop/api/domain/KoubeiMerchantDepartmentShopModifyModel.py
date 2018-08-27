#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SimpleShopModel import SimpleShopModel
from alipay.aop.api.domain.SimpleShopModel import SimpleShopModel


class KoubeiMerchantDepartmentShopModifyModel(object):

    def __init__(self):
        self._auth_code = None
        self._dept_id = None
        self._dept_type = None
        self._shop_list_to_add = None
        self._shop_list_to_remove = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value
    @property
    def dept_type(self):
        return self._dept_type

    @dept_type.setter
    def dept_type(self, value):
        self._dept_type = value
    @property
    def shop_list_to_add(self):
        return self._shop_list_to_add

    @shop_list_to_add.setter
    def shop_list_to_add(self, value):
        if isinstance(value, list):
            self._shop_list_to_add = list()
            for i in value:
                if isinstance(i, SimpleShopModel):
                    self._shop_list_to_add.append(i)
                else:
                    self._shop_list_to_add.append(SimpleShopModel.from_alipay_dict(i))
    @property
    def shop_list_to_remove(self):
        return self._shop_list_to_remove

    @shop_list_to_remove.setter
    def shop_list_to_remove(self, value):
        if isinstance(value, list):
            self._shop_list_to_remove = list()
            for i in value:
                if isinstance(i, SimpleShopModel):
                    self._shop_list_to_remove.append(i)
                else:
                    self._shop_list_to_remove.append(SimpleShopModel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.dept_id:
            if hasattr(self.dept_id, 'to_alipay_dict'):
                params['dept_id'] = self.dept_id.to_alipay_dict()
            else:
                params['dept_id'] = self.dept_id
        if self.dept_type:
            if hasattr(self.dept_type, 'to_alipay_dict'):
                params['dept_type'] = self.dept_type.to_alipay_dict()
            else:
                params['dept_type'] = self.dept_type
        if self.shop_list_to_add:
            if isinstance(self.shop_list_to_add, list):
                for i in range(0, len(self.shop_list_to_add)):
                    element = self.shop_list_to_add[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_list_to_add[i] = element.to_alipay_dict()
            if hasattr(self.shop_list_to_add, 'to_alipay_dict'):
                params['shop_list_to_add'] = self.shop_list_to_add.to_alipay_dict()
            else:
                params['shop_list_to_add'] = self.shop_list_to_add
        if self.shop_list_to_remove:
            if isinstance(self.shop_list_to_remove, list):
                for i in range(0, len(self.shop_list_to_remove)):
                    element = self.shop_list_to_remove[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_list_to_remove[i] = element.to_alipay_dict()
            if hasattr(self.shop_list_to_remove, 'to_alipay_dict'):
                params['shop_list_to_remove'] = self.shop_list_to_remove.to_alipay_dict()
            else:
                params['shop_list_to_remove'] = self.shop_list_to_remove
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMerchantDepartmentShopModifyModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'dept_id' in d:
            o.dept_id = d['dept_id']
        if 'dept_type' in d:
            o.dept_type = d['dept_type']
        if 'shop_list_to_add' in d:
            o.shop_list_to_add = d['shop_list_to_add']
        if 'shop_list_to_remove' in d:
            o.shop_list_to_remove = d['shop_list_to_remove']
        return o


