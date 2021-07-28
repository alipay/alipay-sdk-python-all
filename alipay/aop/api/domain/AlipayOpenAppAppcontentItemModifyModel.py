#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemExt import ItemExt
from alipay.aop.api.domain.ItemProperty import ItemProperty
from alipay.aop.api.domain.ItemUrl import ItemUrl


class AlipayOpenAppAppcontentItemModifyModel(object):

    def __init__(self):
        self._barcode = None
        self._barcode_type = None
        self._biz_extends = None
        self._biz_unique_id = None
        self._category_id = None
        self._custom_properties = None
        self._description = None
        self._detail_pic_paths = None
        self._detail_urls = None
        self._item_id = None
        self._major_pic_path = None
        self._origin_price = None
        self._sale_price = None
        self._status = None
        self._stock_status = None
        self._title = None

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value
    @property
    def barcode_type(self):
        return self._barcode_type

    @barcode_type.setter
    def barcode_type(self, value):
        self._barcode_type = value
    @property
    def biz_extends(self):
        return self._biz_extends

    @biz_extends.setter
    def biz_extends(self, value):
        if isinstance(value, list):
            self._biz_extends = list()
            for i in value:
                if isinstance(i, ItemExt):
                    self._biz_extends.append(i)
                else:
                    self._biz_extends.append(ItemExt.from_alipay_dict(i))
    @property
    def biz_unique_id(self):
        return self._biz_unique_id

    @biz_unique_id.setter
    def biz_unique_id(self, value):
        self._biz_unique_id = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def custom_properties(self):
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, value):
        if isinstance(value, ItemProperty):
            self._custom_properties = value
        else:
            self._custom_properties = ItemProperty.from_alipay_dict(value)
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def detail_pic_paths(self):
        return self._detail_pic_paths

    @detail_pic_paths.setter
    def detail_pic_paths(self, value):
        if isinstance(value, list):
            self._detail_pic_paths = list()
            for i in value:
                self._detail_pic_paths.append(i)
    @property
    def detail_urls(self):
        return self._detail_urls

    @detail_urls.setter
    def detail_urls(self, value):
        if isinstance(value, list):
            self._detail_urls = list()
            for i in value:
                if isinstance(i, ItemUrl):
                    self._detail_urls.append(i)
                else:
                    self._detail_urls.append(ItemUrl.from_alipay_dict(i))
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def major_pic_path(self):
        return self._major_pic_path

    @major_pic_path.setter
    def major_pic_path(self, value):
        self._major_pic_path = value
    @property
    def origin_price(self):
        return self._origin_price

    @origin_price.setter
    def origin_price(self, value):
        self._origin_price = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
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
        if self.barcode:
            if hasattr(self.barcode, 'to_alipay_dict'):
                params['barcode'] = self.barcode.to_alipay_dict()
            else:
                params['barcode'] = self.barcode
        if self.barcode_type:
            if hasattr(self.barcode_type, 'to_alipay_dict'):
                params['barcode_type'] = self.barcode_type.to_alipay_dict()
            else:
                params['barcode_type'] = self.barcode_type
        if self.biz_extends:
            if isinstance(self.biz_extends, list):
                for i in range(0, len(self.biz_extends)):
                    element = self.biz_extends[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_extends[i] = element.to_alipay_dict()
            if hasattr(self.biz_extends, 'to_alipay_dict'):
                params['biz_extends'] = self.biz_extends.to_alipay_dict()
            else:
                params['biz_extends'] = self.biz_extends
        if self.biz_unique_id:
            if hasattr(self.biz_unique_id, 'to_alipay_dict'):
                params['biz_unique_id'] = self.biz_unique_id.to_alipay_dict()
            else:
                params['biz_unique_id'] = self.biz_unique_id
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.custom_properties:
            if hasattr(self.custom_properties, 'to_alipay_dict'):
                params['custom_properties'] = self.custom_properties.to_alipay_dict()
            else:
                params['custom_properties'] = self.custom_properties
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.detail_pic_paths:
            if isinstance(self.detail_pic_paths, list):
                for i in range(0, len(self.detail_pic_paths)):
                    element = self.detail_pic_paths[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detail_pic_paths[i] = element.to_alipay_dict()
            if hasattr(self.detail_pic_paths, 'to_alipay_dict'):
                params['detail_pic_paths'] = self.detail_pic_paths.to_alipay_dict()
            else:
                params['detail_pic_paths'] = self.detail_pic_paths
        if self.detail_urls:
            if isinstance(self.detail_urls, list):
                for i in range(0, len(self.detail_urls)):
                    element = self.detail_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detail_urls[i] = element.to_alipay_dict()
            if hasattr(self.detail_urls, 'to_alipay_dict'):
                params['detail_urls'] = self.detail_urls.to_alipay_dict()
            else:
                params['detail_urls'] = self.detail_urls
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.major_pic_path:
            if hasattr(self.major_pic_path, 'to_alipay_dict'):
                params['major_pic_path'] = self.major_pic_path.to_alipay_dict()
            else:
                params['major_pic_path'] = self.major_pic_path
        if self.origin_price:
            if hasattr(self.origin_price, 'to_alipay_dict'):
                params['origin_price'] = self.origin_price.to_alipay_dict()
            else:
                params['origin_price'] = self.origin_price
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayOpenAppAppcontentItemModifyModel()
        if 'barcode' in d:
            o.barcode = d['barcode']
        if 'barcode_type' in d:
            o.barcode_type = d['barcode_type']
        if 'biz_extends' in d:
            o.biz_extends = d['biz_extends']
        if 'biz_unique_id' in d:
            o.biz_unique_id = d['biz_unique_id']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'custom_properties' in d:
            o.custom_properties = d['custom_properties']
        if 'description' in d:
            o.description = d['description']
        if 'detail_pic_paths' in d:
            o.detail_pic_paths = d['detail_pic_paths']
        if 'detail_urls' in d:
            o.detail_urls = d['detail_urls']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'major_pic_path' in d:
            o.major_pic_path = d['major_pic_path']
        if 'origin_price' in d:
            o.origin_price = d['origin_price']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'status' in d:
            o.status = d['status']
        if 'stock_status' in d:
            o.stock_status = d['stock_status']
        if 'title' in d:
            o.title = d['title']
        return o


