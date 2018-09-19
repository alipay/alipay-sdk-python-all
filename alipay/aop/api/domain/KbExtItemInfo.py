#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BrandLevelInfo import BrandLevelInfo
from alipay.aop.api.domain.CategoryLevelInfo import CategoryLevelInfo


class KbExtItemInfo(object):

    def __init__(self):
        self._brand_level_info_list = None
        self._brief = None
        self._category_level_info_list = None
        self._count = None
        self._country = None
        self._currency = None
        self._description = None
        self._goods_id = None
        self._goods_name = None
        self._inner_goods_id = None
        self._item_format = None
        self._pack = None
        self._picture_id_list = None
        self._price = None
        self._specification = None
        self._unit = None

    @property
    def brand_level_info_list(self):
        return self._brand_level_info_list

    @brand_level_info_list.setter
    def brand_level_info_list(self, value):
        if isinstance(value, list):
            self._brand_level_info_list = list()
            for i in value:
                if isinstance(i, BrandLevelInfo):
                    self._brand_level_info_list.append(i)
                else:
                    self._brand_level_info_list.append(BrandLevelInfo.from_alipay_dict(i))
    @property
    def brief(self):
        return self._brief

    @brief.setter
    def brief(self, value):
        self._brief = value
    @property
    def category_level_info_list(self):
        return self._category_level_info_list

    @category_level_info_list.setter
    def category_level_info_list(self, value):
        if isinstance(value, list):
            self._category_level_info_list = list()
            for i in value:
                if isinstance(i, CategoryLevelInfo):
                    self._category_level_info_list.append(i)
                else:
                    self._category_level_info_list.append(CategoryLevelInfo.from_alipay_dict(i))
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
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
    def inner_goods_id(self):
        return self._inner_goods_id

    @inner_goods_id.setter
    def inner_goods_id(self, value):
        self._inner_goods_id = value
    @property
    def item_format(self):
        return self._item_format

    @item_format.setter
    def item_format(self, value):
        self._item_format = value
    @property
    def pack(self):
        return self._pack

    @pack.setter
    def pack(self, value):
        self._pack = value
    @property
    def picture_id_list(self):
        return self._picture_id_list

    @picture_id_list.setter
    def picture_id_list(self, value):
        if isinstance(value, list):
            self._picture_id_list = list()
            for i in value:
                self._picture_id_list.append(i)
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        self._specification = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_level_info_list:
            if isinstance(self.brand_level_info_list, list):
                for i in range(0, len(self.brand_level_info_list)):
                    element = self.brand_level_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_level_info_list[i] = element.to_alipay_dict()
            if hasattr(self.brand_level_info_list, 'to_alipay_dict'):
                params['brand_level_info_list'] = self.brand_level_info_list.to_alipay_dict()
            else:
                params['brand_level_info_list'] = self.brand_level_info_list
        if self.brief:
            if hasattr(self.brief, 'to_alipay_dict'):
                params['brief'] = self.brief.to_alipay_dict()
            else:
                params['brief'] = self.brief
        if self.category_level_info_list:
            if isinstance(self.category_level_info_list, list):
                for i in range(0, len(self.category_level_info_list)):
                    element = self.category_level_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_level_info_list[i] = element.to_alipay_dict()
            if hasattr(self.category_level_info_list, 'to_alipay_dict'):
                params['category_level_info_list'] = self.category_level_info_list.to_alipay_dict()
            else:
                params['category_level_info_list'] = self.category_level_info_list
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
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
        if self.inner_goods_id:
            if hasattr(self.inner_goods_id, 'to_alipay_dict'):
                params['inner_goods_id'] = self.inner_goods_id.to_alipay_dict()
            else:
                params['inner_goods_id'] = self.inner_goods_id
        if self.item_format:
            if hasattr(self.item_format, 'to_alipay_dict'):
                params['item_format'] = self.item_format.to_alipay_dict()
            else:
                params['item_format'] = self.item_format
        if self.pack:
            if hasattr(self.pack, 'to_alipay_dict'):
                params['pack'] = self.pack.to_alipay_dict()
            else:
                params['pack'] = self.pack
        if self.picture_id_list:
            if isinstance(self.picture_id_list, list):
                for i in range(0, len(self.picture_id_list)):
                    element = self.picture_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.picture_id_list[i] = element.to_alipay_dict()
            if hasattr(self.picture_id_list, 'to_alipay_dict'):
                params['picture_id_list'] = self.picture_id_list.to_alipay_dict()
            else:
                params['picture_id_list'] = self.picture_id_list
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.specification:
            if hasattr(self.specification, 'to_alipay_dict'):
                params['specification'] = self.specification.to_alipay_dict()
            else:
                params['specification'] = self.specification
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbExtItemInfo()
        if 'brand_level_info_list' in d:
            o.brand_level_info_list = d['brand_level_info_list']
        if 'brief' in d:
            o.brief = d['brief']
        if 'category_level_info_list' in d:
            o.category_level_info_list = d['category_level_info_list']
        if 'count' in d:
            o.count = d['count']
        if 'country' in d:
            o.country = d['country']
        if 'currency' in d:
            o.currency = d['currency']
        if 'description' in d:
            o.description = d['description']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'inner_goods_id' in d:
            o.inner_goods_id = d['inner_goods_id']
        if 'item_format' in d:
            o.item_format = d['item_format']
        if 'pack' in d:
            o.pack = d['pack']
        if 'picture_id_list' in d:
            o.picture_id_list = d['picture_id_list']
        if 'price' in d:
            o.price = d['price']
        if 'specification' in d:
            o.specification = d['specification']
        if 'unit' in d:
            o.unit = d['unit']
        return o


