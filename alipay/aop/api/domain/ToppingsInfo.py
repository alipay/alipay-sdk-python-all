#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SpecificationInfo import SpecificationInfo


class ToppingsInfo(object):

    def __init__(self):
        self._category = None
        self._category_id = None
        self._category_name = None
        self._count = None
        self._goods_id = None
        self._goods_name = None
        self._id = None
        self._image = None
        self._inventory = None
        self._name = None
        self._optional_specifications = None
        self._price = None
        self._sku_id = None
        self._spec_id = None
        self._spec_name = None
        self._spu_id = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def optional_specifications(self):
        return self._optional_specifications

    @optional_specifications.setter
    def optional_specifications(self, value):
        if isinstance(value, list):
            self._optional_specifications = list()
            for i in value:
                if isinstance(i, SpecificationInfo):
                    self._optional_specifications.append(i)
                else:
                    self._optional_specifications.append(SpecificationInfo.from_alipay_dict(i))
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def spec_id(self):
        return self._spec_id

    @spec_id.setter
    def spec_id(self, value):
        self._spec_id = value
    @property
    def spec_name(self):
        return self._spec_name

    @spec_name.setter
    def spec_name(self, value):
        self._spec_name = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.optional_specifications:
            if isinstance(self.optional_specifications, list):
                for i in range(0, len(self.optional_specifications)):
                    element = self.optional_specifications[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.optional_specifications[i] = element.to_alipay_dict()
            if hasattr(self.optional_specifications, 'to_alipay_dict'):
                params['optional_specifications'] = self.optional_specifications.to_alipay_dict()
            else:
                params['optional_specifications'] = self.optional_specifications
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.spec_id:
            if hasattr(self.spec_id, 'to_alipay_dict'):
                params['spec_id'] = self.spec_id.to_alipay_dict()
            else:
                params['spec_id'] = self.spec_id
        if self.spec_name:
            if hasattr(self.spec_name, 'to_alipay_dict'):
                params['spec_name'] = self.spec_name.to_alipay_dict()
            else:
                params['spec_name'] = self.spec_name
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ToppingsInfo()
        if 'category' in d:
            o.category = d['category']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'count' in d:
            o.count = d['count']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'id' in d:
            o.id = d['id']
        if 'image' in d:
            o.image = d['image']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'name' in d:
            o.name = d['name']
        if 'optional_specifications' in d:
            o.optional_specifications = d['optional_specifications']
        if 'price' in d:
            o.price = d['price']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'spec_id' in d:
            o.spec_id = d['spec_id']
        if 'spec_name' in d:
            o.spec_name = d['spec_name']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        return o


