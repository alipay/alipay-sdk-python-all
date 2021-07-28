#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpuDetail(object):

    def __init__(self):
        self._brand = None
        self._category = None
        self._dimension = None
        self._icon = None
        self._link_url = None
        self._spu_id = None
        self._title = None

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
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        self._dimension = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.dimension:
            if hasattr(self.dimension, 'to_alipay_dict'):
                params['dimension'] = self.dimension.to_alipay_dict()
            else:
                params['dimension'] = self.dimension
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
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
        o = SpuDetail()
        if 'brand' in d:
            o.brand = d['brand']
        if 'category' in d:
            o.category = d['category']
        if 'dimension' in d:
            o.dimension = d['dimension']
        if 'icon' in d:
            o.icon = d['icon']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'title' in d:
            o.title = d['title']
        return o


