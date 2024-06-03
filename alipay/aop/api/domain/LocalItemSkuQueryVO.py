#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemSkuAttrVO import ItemSkuAttrVO


class LocalItemSkuQueryVO(object):

    def __init__(self):
        self._attrs = None
        self._original_price = None
        self._out_sku_id = None
        self._sale_price = None
        self._sale_status = None
        self._sku_id = None
        self._stock_num = None
        self._thumb_img_url = None

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        if isinstance(value, list):
            self._attrs = list()
            for i in value:
                if isinstance(i, ItemSkuAttrVO):
                    self._attrs.append(i)
                else:
                    self._attrs.append(ItemSkuAttrVO.from_alipay_dict(i))
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
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
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def thumb_img_url(self):
        return self._thumb_img_url

    @thumb_img_url.setter
    def thumb_img_url(self, value):
        self._thumb_img_url = value


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
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
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
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        if self.thumb_img_url:
            if hasattr(self.thumb_img_url, 'to_alipay_dict'):
                params['thumb_img_url'] = self.thumb_img_url.to_alipay_dict()
            else:
                params['thumb_img_url'] = self.thumb_img_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LocalItemSkuQueryVO()
        if 'attrs' in d:
            o.attrs = d['attrs']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sale_status' in d:
            o.sale_status = d['sale_status']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        if 'thumb_img_url' in d:
            o.thumb_img_url = d['thumb_img_url']
        return o


