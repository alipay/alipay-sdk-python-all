#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemAttrVO import AppItemAttrVO
from alipay.aop.api.domain.ItemDescInfoVO import ItemDescInfoVO
from alipay.aop.api.domain.ItemSkuCreateVO import ItemSkuCreateVO


class AlipayOpenAppItemCreateModel(object):

    def __init__(self):
        self._attrs = None
        self._barcode = None
        self._category_id = None
        self._desc = None
        self._desc_info = None
        self._direct_path = None
        self._head_img = None
        self._image_list = None
        self._item_details_page_model = None
        self._item_type = None
        self._original_price = None
        self._out_item_id = None
        self._path = None
        self._price_unit = None
        self._sale_price = None
        self._sale_status = None
        self._skus = None
        self._stock_num = None
        self._title = None

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        if isinstance(value, list):
            self._attrs = list()
            for i in value:
                if isinstance(i, AppItemAttrVO):
                    self._attrs.append(i)
                else:
                    self._attrs.append(AppItemAttrVO.from_alipay_dict(i))
    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def desc_info(self):
        return self._desc_info

    @desc_info.setter
    def desc_info(self, value):
        if isinstance(value, ItemDescInfoVO):
            self._desc_info = value
        else:
            self._desc_info = ItemDescInfoVO.from_alipay_dict(value)
    @property
    def direct_path(self):
        return self._direct_path

    @direct_path.setter
    def direct_path(self, value):
        self._direct_path = value
    @property
    def head_img(self):
        return self._head_img

    @head_img.setter
    def head_img(self, value):
        self._head_img = value
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
    def item_details_page_model(self):
        return self._item_details_page_model

    @item_details_page_model.setter
    def item_details_page_model(self, value):
        self._item_details_page_model = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def price_unit(self):
        return self._price_unit

    @price_unit.setter
    def price_unit(self, value):
        self._price_unit = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sale_status(self):
        return self._sale_status

    @sale_status.setter
    def sale_status(self, value):
        self._sale_status = value
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, ItemSkuCreateVO):
                    self._skus.append(i)
                else:
                    self._skus.append(ItemSkuCreateVO.from_alipay_dict(i))
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.attrs:
            if isinstance(self.attrs, list):
                for i in range(0, len(self.attrs)):
                    element = self.attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attrs[i] = element.to_alipay_dict()
            if hasattr(self.attrs, 'to_alipay_dict'):
                params['attrs'] = self.attrs.to_alipay_dict()
            else:
                params['attrs'] = self.attrs
        if self.barcode:
            if hasattr(self.barcode, 'to_alipay_dict'):
                params['barcode'] = self.barcode.to_alipay_dict()
            else:
                params['barcode'] = self.barcode
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.desc_info:
            if hasattr(self.desc_info, 'to_alipay_dict'):
                params['desc_info'] = self.desc_info.to_alipay_dict()
            else:
                params['desc_info'] = self.desc_info
        if self.direct_path:
            if hasattr(self.direct_path, 'to_alipay_dict'):
                params['direct_path'] = self.direct_path.to_alipay_dict()
            else:
                params['direct_path'] = self.direct_path
        if self.head_img:
            if hasattr(self.head_img, 'to_alipay_dict'):
                params['head_img'] = self.head_img.to_alipay_dict()
            else:
                params['head_img'] = self.head_img
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
        if self.item_details_page_model:
            if hasattr(self.item_details_page_model, 'to_alipay_dict'):
                params['item_details_page_model'] = self.item_details_page_model.to_alipay_dict()
            else:
                params['item_details_page_model'] = self.item_details_page_model
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.price_unit:
            if hasattr(self.price_unit, 'to_alipay_dict'):
                params['price_unit'] = self.price_unit.to_alipay_dict()
            else:
                params['price_unit'] = self.price_unit
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sale_status:
            if hasattr(self.sale_status, 'to_alipay_dict'):
                params['sale_status'] = self.sale_status.to_alipay_dict()
            else:
                params['sale_status'] = self.sale_status
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
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
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
        o = AlipayOpenAppItemCreateModel()
        if 'attrs' in d:
            o.attrs = d['attrs']
        if 'barcode' in d:
            o.barcode = d['barcode']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'desc' in d:
            o.desc = d['desc']
        if 'desc_info' in d:
            o.desc_info = d['desc_info']
        if 'direct_path' in d:
            o.direct_path = d['direct_path']
        if 'head_img' in d:
            o.head_img = d['head_img']
        if 'image_list' in d:
            o.image_list = d['image_list']
        if 'item_details_page_model' in d:
            o.item_details_page_model = d['item_details_page_model']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'path' in d:
            o.path = d['path']
        if 'price_unit' in d:
            o.price_unit = d['price_unit']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sale_status' in d:
            o.sale_status = d['sale_status']
        if 'skus' in d:
            o.skus = d['skus']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        if 'title' in d:
            o.title = d['title']
        return o


