#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PermissionSetVO import PermissionSetVO


class FrontProductVO(object):

    def __init__(self):
        self._permission_set_list = None
        self._product_code = None
        self._product_name = None

    @property
    def permission_set_list(self):
        return self._permission_set_list

    @permission_set_list.setter
    def permission_set_list(self, value):
        if isinstance(value, list):
            self._permission_set_list = list()
            for i in value:
                if isinstance(i, PermissionSetVO):
                    self._permission_set_list.append(i)
                else:
                    self._permission_set_list.append(PermissionSetVO.from_alipay_dict(i))
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.permission_set_list:
            if isinstance(self.permission_set_list, list):
                for i in range(0, len(self.permission_set_list)):
                    element = self.permission_set_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.permission_set_list[i] = element.to_alipay_dict()
            if hasattr(self.permission_set_list, 'to_alipay_dict'):
                params['permission_set_list'] = self.permission_set_list.to_alipay_dict()
            else:
                params['permission_set_list'] = self.permission_set_list
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
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
        o = FrontProductVO()
        if 'permission_set_list' in d:
            o.permission_set_list = d['permission_set_list']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_name' in d:
            o.product_name = d['product_name']
        return o


