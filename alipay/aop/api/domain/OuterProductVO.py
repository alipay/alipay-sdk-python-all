#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ModuleVO import ModuleVO


class OuterProductVO(object):

    def __init__(self):
        self._module_items = None
        self._outer_product_code = None
        self._outer_product_id = None

    @property
    def module_items(self):
        return self._module_items

    @module_items.setter
    def module_items(self, value):
        if isinstance(value, list):
            self._module_items = list()
            for i in value:
                if isinstance(i, ModuleVO):
                    self._module_items.append(i)
                else:
                    self._module_items.append(ModuleVO.from_alipay_dict(i))
    @property
    def outer_product_code(self):
        return self._outer_product_code

    @outer_product_code.setter
    def outer_product_code(self, value):
        self._outer_product_code = value
    @property
    def outer_product_id(self):
        return self._outer_product_id

    @outer_product_id.setter
    def outer_product_id(self, value):
        self._outer_product_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.module_items:
            if isinstance(self.module_items, list):
                for i in range(0, len(self.module_items)):
                    element = self.module_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.module_items[i] = element.to_alipay_dict()
            if hasattr(self.module_items, 'to_alipay_dict'):
                params['module_items'] = self.module_items.to_alipay_dict()
            else:
                params['module_items'] = self.module_items
        if self.outer_product_code:
            if hasattr(self.outer_product_code, 'to_alipay_dict'):
                params['outer_product_code'] = self.outer_product_code.to_alipay_dict()
            else:
                params['outer_product_code'] = self.outer_product_code
        if self.outer_product_id:
            if hasattr(self.outer_product_id, 'to_alipay_dict'):
                params['outer_product_id'] = self.outer_product_id.to_alipay_dict()
            else:
                params['outer_product_id'] = self.outer_product_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OuterProductVO()
        if 'module_items' in d:
            o.module_items = d['module_items']
        if 'outer_product_code' in d:
            o.outer_product_code = d['outer_product_code']
        if 'outer_product_id' in d:
            o.outer_product_id = d['outer_product_id']
        return o


