#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SpuAttribute import SpuAttribute


class AlipayIserviceCcmSwSpuSyncModel(object):

    def __init__(self):
        self._attribute = None
        self._brand = None
        self._category = None
        self._description = None
        self._icon = None
        self._is_delete = None
        self._library_id = None
        self._library_name = None
        self._link_url = None
        self._original_price = None
        self._price = None
        self._spu_id = None
        self._status = None
        self._title = None

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        if isinstance(value, list):
            self._attribute = list()
            for i in value:
                if isinstance(i, SpuAttribute):
                    self._attribute.append(i)
                else:
                    self._attribute.append(SpuAttribute.from_alipay_dict(i))
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def is_delete(self):
        return self._is_delete

    @is_delete.setter
    def is_delete(self, value):
        self._is_delete = value
    @property
    def library_id(self):
        return self._library_id

    @library_id.setter
    def library_id(self, value):
        self._library_id = value
    @property
    def library_name(self):
        return self._library_name

    @library_name.setter
    def library_name(self, value):
        self._library_name = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.attribute:
            if isinstance(self.attribute, list):
                for i in range(0, len(self.attribute)):
                    element = self.attribute[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attribute[i] = element.to_alipay_dict()
            if hasattr(self.attribute, 'to_alipay_dict'):
                params['attribute'] = self.attribute.to_alipay_dict()
            else:
                params['attribute'] = self.attribute
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.is_delete:
            if hasattr(self.is_delete, 'to_alipay_dict'):
                params['is_delete'] = self.is_delete.to_alipay_dict()
            else:
                params['is_delete'] = self.is_delete
        if self.library_id:
            if hasattr(self.library_id, 'to_alipay_dict'):
                params['library_id'] = self.library_id.to_alipay_dict()
            else:
                params['library_id'] = self.library_id
        if self.library_name:
            if hasattr(self.library_name, 'to_alipay_dict'):
                params['library_name'] = self.library_name.to_alipay_dict()
            else:
                params['library_name'] = self.library_name
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayIserviceCcmSwSpuSyncModel()
        if 'attribute' in d:
            o.attribute = d['attribute']
        if 'brand' in d:
            o.brand = d['brand']
        if 'category' in d:
            o.category = d['category']
        if 'description' in d:
            o.description = d['description']
        if 'icon' in d:
            o.icon = d['icon']
        if 'is_delete' in d:
            o.is_delete = d['is_delete']
        if 'library_id' in d:
            o.library_id = d['library_id']
        if 'library_name' in d:
            o.library_name = d['library_name']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'price' in d:
            o.price = d['price']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'status' in d:
            o.status = d['status']
        if 'title' in d:
            o.title = d['title']
        return o


