#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishMaterialSimplifyInfo import KbdishMaterialSimplifyInfo


class KbdishSkuSimplifyInfo(object):

    def __init__(self):
        self._material_group_list = None
        self._out_sku_id = None
        self._price = None
        self._spec_01_group_name = None
        self._spec_01_id = None
        self._spec_01_name = None
        self._spec_01_sort = None
        self._spec_02_group_name = None
        self._spec_02_id = None
        self._spec_02_name = None
        self._spec_02_sort = None

    @property
    def material_group_list(self):
        return self._material_group_list

    @material_group_list.setter
    def material_group_list(self, value):
        if isinstance(value, list):
            self._material_group_list = list()
            for i in value:
                if isinstance(i, KbdishMaterialSimplifyInfo):
                    self._material_group_list.append(i)
                else:
                    self._material_group_list.append(KbdishMaterialSimplifyInfo.from_alipay_dict(i))
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def spec_01_group_name(self):
        return self._spec_01_group_name

    @spec_01_group_name.setter
    def spec_01_group_name(self, value):
        self._spec_01_group_name = value
    @property
    def spec_01_id(self):
        return self._spec_01_id

    @spec_01_id.setter
    def spec_01_id(self, value):
        self._spec_01_id = value
    @property
    def spec_01_name(self):
        return self._spec_01_name

    @spec_01_name.setter
    def spec_01_name(self, value):
        self._spec_01_name = value
    @property
    def spec_01_sort(self):
        return self._spec_01_sort

    @spec_01_sort.setter
    def spec_01_sort(self, value):
        self._spec_01_sort = value
    @property
    def spec_02_group_name(self):
        return self._spec_02_group_name

    @spec_02_group_name.setter
    def spec_02_group_name(self, value):
        self._spec_02_group_name = value
    @property
    def spec_02_id(self):
        return self._spec_02_id

    @spec_02_id.setter
    def spec_02_id(self, value):
        self._spec_02_id = value
    @property
    def spec_02_name(self):
        return self._spec_02_name

    @spec_02_name.setter
    def spec_02_name(self, value):
        self._spec_02_name = value
    @property
    def spec_02_sort(self):
        return self._spec_02_sort

    @spec_02_sort.setter
    def spec_02_sort(self, value):
        self._spec_02_sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.material_group_list:
            if isinstance(self.material_group_list, list):
                for i in range(0, len(self.material_group_list)):
                    element = self.material_group_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_group_list[i] = element.to_alipay_dict()
            if hasattr(self.material_group_list, 'to_alipay_dict'):
                params['material_group_list'] = self.material_group_list.to_alipay_dict()
            else:
                params['material_group_list'] = self.material_group_list
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.spec_01_group_name:
            if hasattr(self.spec_01_group_name, 'to_alipay_dict'):
                params['spec_01_group_name'] = self.spec_01_group_name.to_alipay_dict()
            else:
                params['spec_01_group_name'] = self.spec_01_group_name
        if self.spec_01_id:
            if hasattr(self.spec_01_id, 'to_alipay_dict'):
                params['spec_01_id'] = self.spec_01_id.to_alipay_dict()
            else:
                params['spec_01_id'] = self.spec_01_id
        if self.spec_01_name:
            if hasattr(self.spec_01_name, 'to_alipay_dict'):
                params['spec_01_name'] = self.spec_01_name.to_alipay_dict()
            else:
                params['spec_01_name'] = self.spec_01_name
        if self.spec_01_sort:
            if hasattr(self.spec_01_sort, 'to_alipay_dict'):
                params['spec_01_sort'] = self.spec_01_sort.to_alipay_dict()
            else:
                params['spec_01_sort'] = self.spec_01_sort
        if self.spec_02_group_name:
            if hasattr(self.spec_02_group_name, 'to_alipay_dict'):
                params['spec_02_group_name'] = self.spec_02_group_name.to_alipay_dict()
            else:
                params['spec_02_group_name'] = self.spec_02_group_name
        if self.spec_02_id:
            if hasattr(self.spec_02_id, 'to_alipay_dict'):
                params['spec_02_id'] = self.spec_02_id.to_alipay_dict()
            else:
                params['spec_02_id'] = self.spec_02_id
        if self.spec_02_name:
            if hasattr(self.spec_02_name, 'to_alipay_dict'):
                params['spec_02_name'] = self.spec_02_name.to_alipay_dict()
            else:
                params['spec_02_name'] = self.spec_02_name
        if self.spec_02_sort:
            if hasattr(self.spec_02_sort, 'to_alipay_dict'):
                params['spec_02_sort'] = self.spec_02_sort.to_alipay_dict()
            else:
                params['spec_02_sort'] = self.spec_02_sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishSkuSimplifyInfo()
        if 'material_group_list' in d:
            o.material_group_list = d['material_group_list']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'price' in d:
            o.price = d['price']
        if 'spec_01_group_name' in d:
            o.spec_01_group_name = d['spec_01_group_name']
        if 'spec_01_id' in d:
            o.spec_01_id = d['spec_01_id']
        if 'spec_01_name' in d:
            o.spec_01_name = d['spec_01_name']
        if 'spec_01_sort' in d:
            o.spec_01_sort = d['spec_01_sort']
        if 'spec_02_group_name' in d:
            o.spec_02_group_name = d['spec_02_group_name']
        if 'spec_02_id' in d:
            o.spec_02_id = d['spec_02_id']
        if 'spec_02_name' in d:
            o.spec_02_name = d['spec_02_name']
        if 'spec_02_sort' in d:
            o.spec_02_sort = d['spec_02_sort']
        return o


