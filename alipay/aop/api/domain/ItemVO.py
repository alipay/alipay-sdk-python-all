#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BarcodeInfoVO import BarcodeInfoVO
from alipay.aop.api.domain.ItemCategoryVO import ItemCategoryVO


class ItemVO(object):

    def __init__(self):
        self._barcode_info = None
        self._can_be_search = None
        self._desc = None
        self._feature = None
        self._image_list = None
        self._item_id = None
        self._main_image = None
        self._original_price = None
        self._platform_category = None
        self._platform_item_id = None
        self._price = None
        self._src_path = None
        self._stock_status = None
        self._title = None

    @property
    def barcode_info(self):
        return self._barcode_info

    @barcode_info.setter
    def barcode_info(self, value):
        if isinstance(value, BarcodeInfoVO):
            self._barcode_info = value
        else:
            self._barcode_info = BarcodeInfoVO.from_alipay_dict(value)
    @property
    def can_be_search(self):
        return self._can_be_search

    @can_be_search.setter
    def can_be_search(self, value):
        self._can_be_search = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def feature(self):
        return self._feature

    @feature.setter
    def feature(self, value):
        self._feature = value
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                self._image_list.append(i)
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def main_image(self):
        return self._main_image

    @main_image.setter
    def main_image(self, value):
        self._main_image = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def platform_category(self):
        return self._platform_category

    @platform_category.setter
    def platform_category(self, value):
        if isinstance(value, ItemCategoryVO):
            self._platform_category = value
        else:
            self._platform_category = ItemCategoryVO.from_alipay_dict(value)
    @property
    def platform_item_id(self):
        return self._platform_item_id

    @platform_item_id.setter
    def platform_item_id(self, value):
        self._platform_item_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def src_path(self):
        return self._src_path

    @src_path.setter
    def src_path(self, value):
        self._src_path = value
    @property
    def stock_status(self):
        return self._stock_status

    @stock_status.setter
    def stock_status(self, value):
        self._stock_status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.barcode_info:
            if hasattr(self.barcode_info, 'to_alipay_dict'):
                params['barcode_info'] = self.barcode_info.to_alipay_dict()
            else:
                params['barcode_info'] = self.barcode_info
        if self.can_be_search:
            if hasattr(self.can_be_search, 'to_alipay_dict'):
                params['can_be_search'] = self.can_be_search.to_alipay_dict()
            else:
                params['can_be_search'] = self.can_be_search
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.feature:
            if hasattr(self.feature, 'to_alipay_dict'):
                params['feature'] = self.feature.to_alipay_dict()
            else:
                params['feature'] = self.feature
        if self.image_list:
            if isinstance(self.image_list, list):
                for i in range(0, len(self.image_list)):
                    element = self.image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_list[i] = element.to_alipay_dict()
            if hasattr(self.image_list, 'to_alipay_dict'):
                params['image_list'] = self.image_list.to_alipay_dict()
            else:
                params['image_list'] = self.image_list
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.main_image:
            if hasattr(self.main_image, 'to_alipay_dict'):
                params['main_image'] = self.main_image.to_alipay_dict()
            else:
                params['main_image'] = self.main_image
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.platform_category:
            if hasattr(self.platform_category, 'to_alipay_dict'):
                params['platform_category'] = self.platform_category.to_alipay_dict()
            else:
                params['platform_category'] = self.platform_category
        if self.platform_item_id:
            if hasattr(self.platform_item_id, 'to_alipay_dict'):
                params['platform_item_id'] = self.platform_item_id.to_alipay_dict()
            else:
                params['platform_item_id'] = self.platform_item_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.src_path:
            if hasattr(self.src_path, 'to_alipay_dict'):
                params['src_path'] = self.src_path.to_alipay_dict()
            else:
                params['src_path'] = self.src_path
        if self.stock_status:
            if hasattr(self.stock_status, 'to_alipay_dict'):
                params['stock_status'] = self.stock_status.to_alipay_dict()
            else:
                params['stock_status'] = self.stock_status
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
        o = ItemVO()
        if 'barcode_info' in d:
            o.barcode_info = d['barcode_info']
        if 'can_be_search' in d:
            o.can_be_search = d['can_be_search']
        if 'desc' in d:
            o.desc = d['desc']
        if 'feature' in d:
            o.feature = d['feature']
        if 'image_list' in d:
            o.image_list = d['image_list']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'main_image' in d:
            o.main_image = d['main_image']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'platform_category' in d:
            o.platform_category = d['platform_category']
        if 'platform_item_id' in d:
            o.platform_item_id = d['platform_item_id']
        if 'price' in d:
            o.price = d['price']
        if 'src_path' in d:
            o.src_path = d['src_path']
        if 'stock_status' in d:
            o.stock_status = d['stock_status']
        if 'title' in d:
            o.title = d['title']
        return o


