#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductProperty import ProductProperty
from alipay.aop.api.domain.LmCategoryVO import LmCategoryVO
from alipay.aop.api.domain.MpcLmSkuVO import MpcLmSkuVO
from alipay.aop.api.domain.ProductProperty import ProductProperty


class MpcLMItemVO(object):

    def __init__(self):
        self._attr = None
        self._brand = None
        self._can_sell = None
        self._category_chain = None
        self._category_id = None
        self._desc_path = None
        self._division_code = None
        self._fuzzy_quantity = None
        self._img_url = None
        self._main_pic = None
        self._mpc_item_id = None
        self._mpc_sku_vo = None
        self._product_properties = None
        self._product_status = None
        self._product_type = None
        self._shop_id = None
        self._sold_quantity = None
        self._tax_code = None
        self._tax_rate = None
        self._title = None

    @property
    def attr(self):
        return self._attr

    @attr.setter
    def attr(self, value):
        if isinstance(value, list):
            self._attr = list()
            for i in value:
                if isinstance(i, ProductProperty):
                    self._attr.append(i)
                else:
                    self._attr.append(ProductProperty.from_alipay_dict(i))
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
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
        if isinstance(value, LmCategoryVO):
            self._category_chain = value
        else:
            self._category_chain = LmCategoryVO.from_alipay_dict(value)
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
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
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def main_pic(self):
        return self._main_pic

    @main_pic.setter
    def main_pic(self, value):
        self._main_pic = value
    @property
    def mpc_item_id(self):
        return self._mpc_item_id

    @mpc_item_id.setter
    def mpc_item_id(self, value):
        self._mpc_item_id = value
    @property
    def mpc_sku_vo(self):
        return self._mpc_sku_vo

    @mpc_sku_vo.setter
    def mpc_sku_vo(self, value):
        if isinstance(value, list):
            self._mpc_sku_vo = list()
            for i in value:
                if isinstance(i, MpcLmSkuVO):
                    self._mpc_sku_vo.append(i)
                else:
                    self._mpc_sku_vo.append(MpcLmSkuVO.from_alipay_dict(i))
    @property
    def product_properties(self):
        return self._product_properties

    @product_properties.setter
    def product_properties(self, value):
        if isinstance(value, list):
            self._product_properties = list()
            for i in value:
                if isinstance(i, ProductProperty):
                    self._product_properties.append(i)
                else:
                    self._product_properties.append(ProductProperty.from_alipay_dict(i))
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
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
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
        if self.attr:
            if isinstance(self.attr, list):
                for i in range(0, len(self.attr)):
                    element = self.attr[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attr[i] = element.to_alipay_dict()
            if hasattr(self.attr, 'to_alipay_dict'):
                params['attr'] = self.attr.to_alipay_dict()
            else:
                params['attr'] = self.attr
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.can_sell:
            if hasattr(self.can_sell, 'to_alipay_dict'):
                params['can_sell'] = self.can_sell.to_alipay_dict()
            else:
                params['can_sell'] = self.can_sell
        if self.category_chain:
            if hasattr(self.category_chain, 'to_alipay_dict'):
                params['category_chain'] = self.category_chain.to_alipay_dict()
            else:
                params['category_chain'] = self.category_chain
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
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
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.main_pic:
            if hasattr(self.main_pic, 'to_alipay_dict'):
                params['main_pic'] = self.main_pic.to_alipay_dict()
            else:
                params['main_pic'] = self.main_pic
        if self.mpc_item_id:
            if hasattr(self.mpc_item_id, 'to_alipay_dict'):
                params['mpc_item_id'] = self.mpc_item_id.to_alipay_dict()
            else:
                params['mpc_item_id'] = self.mpc_item_id
        if self.mpc_sku_vo:
            if isinstance(self.mpc_sku_vo, list):
                for i in range(0, len(self.mpc_sku_vo)):
                    element = self.mpc_sku_vo[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mpc_sku_vo[i] = element.to_alipay_dict()
            if hasattr(self.mpc_sku_vo, 'to_alipay_dict'):
                params['mpc_sku_vo'] = self.mpc_sku_vo.to_alipay_dict()
            else:
                params['mpc_sku_vo'] = self.mpc_sku_vo
        if self.product_properties:
            if isinstance(self.product_properties, list):
                for i in range(0, len(self.product_properties)):
                    element = self.product_properties[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_properties[i] = element.to_alipay_dict()
            if hasattr(self.product_properties, 'to_alipay_dict'):
                params['product_properties'] = self.product_properties.to_alipay_dict()
            else:
                params['product_properties'] = self.product_properties
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
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
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
        o = MpcLMItemVO()
        if 'attr' in d:
            o.attr = d['attr']
        if 'brand' in d:
            o.brand = d['brand']
        if 'can_sell' in d:
            o.can_sell = d['can_sell']
        if 'category_chain' in d:
            o.category_chain = d['category_chain']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'desc_path' in d:
            o.desc_path = d['desc_path']
        if 'division_code' in d:
            o.division_code = d['division_code']
        if 'fuzzy_quantity' in d:
            o.fuzzy_quantity = d['fuzzy_quantity']
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'main_pic' in d:
            o.main_pic = d['main_pic']
        if 'mpc_item_id' in d:
            o.mpc_item_id = d['mpc_item_id']
        if 'mpc_sku_vo' in d:
            o.mpc_sku_vo = d['mpc_sku_vo']
        if 'product_properties' in d:
            o.product_properties = d['product_properties']
        if 'product_status' in d:
            o.product_status = d['product_status']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sold_quantity' in d:
            o.sold_quantity = d['sold_quantity']
        if 'tax_code' in d:
            o.tax_code = d['tax_code']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'title' in d:
            o.title = d['title']
        return o


