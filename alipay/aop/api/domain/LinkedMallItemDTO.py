#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LmCategoryVO import LmCategoryVO
from alipay.aop.api.domain.LinkedMallItemSpecDTO import LinkedMallItemSpecDTO
from alipay.aop.api.domain.LinkedMallItemPropDTO import LinkedMallItemPropDTO
from alipay.aop.api.domain.LinkedMallSkuDTO import LinkedMallSkuDTO


class LinkedMallItemDTO(object):

    def __init__(self):
        self._brand_name = None
        self._can_sell = None
        self._category_chain = None
        self._category_leaf_id = None
        self._desc_path = None
        self._division_code = None
        self._fuzzy_quantity = None
        self._images = None
        self._pic_url = None
        self._product_id = None
        self._product_specs = None
        self._product_status = None
        self._product_type = None
        self._properties = None
        self._quantity = None
        self._shop_id = None
        self._skus = None
        self._sold_quantity = None
        self._tax_code = None
        self._tax_rate = None
        self._title = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def can_sell(self):
        return self._can_sell

    @can_sell.setter
    def can_sell(self, value):
        self._can_sell = value
    @property
    def category_chain(self):
        return self._category_chain

    @category_chain.setter
    def category_chain(self, value):
        if isinstance(value, list):
            self._category_chain = list()
            for i in value:
                if isinstance(i, LmCategoryVO):
                    self._category_chain.append(i)
                else:
                    self._category_chain.append(LmCategoryVO.from_alipay_dict(i))
    @property
    def category_leaf_id(self):
        return self._category_leaf_id

    @category_leaf_id.setter
    def category_leaf_id(self, value):
        self._category_leaf_id = value
    @property
    def desc_path(self):
        return self._desc_path

    @desc_path.setter
    def desc_path(self, value):
        self._desc_path = value
    @property
    def division_code(self):
        return self._division_code

    @division_code.setter
    def division_code(self, value):
        self._division_code = value
    @property
    def fuzzy_quantity(self):
        return self._fuzzy_quantity

    @fuzzy_quantity.setter
    def fuzzy_quantity(self, value):
        self._fuzzy_quantity = value
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if isinstance(value, list):
            self._images = list()
            for i in value:
                self._images.append(i)
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_specs(self):
        return self._product_specs

    @product_specs.setter
    def product_specs(self, value):
        if isinstance(value, list):
            self._product_specs = list()
            for i in value:
                if isinstance(i, LinkedMallItemSpecDTO):
                    self._product_specs.append(i)
                else:
                    self._product_specs.append(LinkedMallItemSpecDTO.from_alipay_dict(i))
    @property
    def product_status(self):
        return self._product_status

    @product_status.setter
    def product_status(self, value):
        self._product_status = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        if isinstance(value, list):
            self._properties = list()
            for i in value:
                if isinstance(i, LinkedMallItemPropDTO):
                    self._properties.append(i)
                else:
                    self._properties.append(LinkedMallItemPropDTO.from_alipay_dict(i))
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, LinkedMallSkuDTO):
                    self._skus.append(i)
                else:
                    self._skus.append(LinkedMallSkuDTO.from_alipay_dict(i))
    @property
    def sold_quantity(self):
        return self._sold_quantity

    @sold_quantity.setter
    def sold_quantity(self, value):
        self._sold_quantity = value
    @property
    def tax_code(self):
        return self._tax_code

    @tax_code.setter
    def tax_code(self, value):
        self._tax_code = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.can_sell:
            if hasattr(self.can_sell, 'to_alipay_dict'):
                params['can_sell'] = self.can_sell.to_alipay_dict()
            else:
                params['can_sell'] = self.can_sell
        if self.category_chain:
            if isinstance(self.category_chain, list):
                for i in range(0, len(self.category_chain)):
                    element = self.category_chain[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_chain[i] = element.to_alipay_dict()
            if hasattr(self.category_chain, 'to_alipay_dict'):
                params['category_chain'] = self.category_chain.to_alipay_dict()
            else:
                params['category_chain'] = self.category_chain
        if self.category_leaf_id:
            if hasattr(self.category_leaf_id, 'to_alipay_dict'):
                params['category_leaf_id'] = self.category_leaf_id.to_alipay_dict()
            else:
                params['category_leaf_id'] = self.category_leaf_id
        if self.desc_path:
            if hasattr(self.desc_path, 'to_alipay_dict'):
                params['desc_path'] = self.desc_path.to_alipay_dict()
            else:
                params['desc_path'] = self.desc_path
        if self.division_code:
            if hasattr(self.division_code, 'to_alipay_dict'):
                params['division_code'] = self.division_code.to_alipay_dict()
            else:
                params['division_code'] = self.division_code
        if self.fuzzy_quantity:
            if hasattr(self.fuzzy_quantity, 'to_alipay_dict'):
                params['fuzzy_quantity'] = self.fuzzy_quantity.to_alipay_dict()
            else:
                params['fuzzy_quantity'] = self.fuzzy_quantity
        if self.images:
            if isinstance(self.images, list):
                for i in range(0, len(self.images)):
                    element = self.images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.images[i] = element.to_alipay_dict()
            if hasattr(self.images, 'to_alipay_dict'):
                params['images'] = self.images.to_alipay_dict()
            else:
                params['images'] = self.images
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_specs:
            if isinstance(self.product_specs, list):
                for i in range(0, len(self.product_specs)):
                    element = self.product_specs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_specs[i] = element.to_alipay_dict()
            if hasattr(self.product_specs, 'to_alipay_dict'):
                params['product_specs'] = self.product_specs.to_alipay_dict()
            else:
                params['product_specs'] = self.product_specs
        if self.product_status:
            if hasattr(self.product_status, 'to_alipay_dict'):
                params['product_status'] = self.product_status.to_alipay_dict()
            else:
                params['product_status'] = self.product_status
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.properties:
            if isinstance(self.properties, list):
                for i in range(0, len(self.properties)):
                    element = self.properties[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.properties[i] = element.to_alipay_dict()
            if hasattr(self.properties, 'to_alipay_dict'):
                params['properties'] = self.properties.to_alipay_dict()
            else:
                params['properties'] = self.properties
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.skus:
            if isinstance(self.skus, list):
                for i in range(0, len(self.skus)):
                    element = self.skus[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skus[i] = element.to_alipay_dict()
            if hasattr(self.skus, 'to_alipay_dict'):
                params['skus'] = self.skus.to_alipay_dict()
            else:
                params['skus'] = self.skus
        if self.sold_quantity:
            if hasattr(self.sold_quantity, 'to_alipay_dict'):
                params['sold_quantity'] = self.sold_quantity.to_alipay_dict()
            else:
                params['sold_quantity'] = self.sold_quantity
        if self.tax_code:
            if hasattr(self.tax_code, 'to_alipay_dict'):
                params['tax_code'] = self.tax_code.to_alipay_dict()
            else:
                params['tax_code'] = self.tax_code
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LinkedMallItemDTO()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'can_sell' in d:
            o.can_sell = d['can_sell']
        if 'category_chain' in d:
            o.category_chain = d['category_chain']
        if 'category_leaf_id' in d:
            o.category_leaf_id = d['category_leaf_id']
        if 'desc_path' in d:
            o.desc_path = d['desc_path']
        if 'division_code' in d:
            o.division_code = d['division_code']
        if 'fuzzy_quantity' in d:
            o.fuzzy_quantity = d['fuzzy_quantity']
        if 'images' in d:
            o.images = d['images']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_specs' in d:
            o.product_specs = d['product_specs']
        if 'product_status' in d:
            o.product_status = d['product_status']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'properties' in d:
            o.properties = d['properties']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'skus' in d:
            o.skus = d['skus']
        if 'sold_quantity' in d:
            o.sold_quantity = d['sold_quantity']
        if 'tax_code' in d:
            o.tax_code = d['tax_code']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'title' in d:
            o.title = d['title']
        return o


