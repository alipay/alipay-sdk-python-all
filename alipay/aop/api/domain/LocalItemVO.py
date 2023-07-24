#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemAttrVO import AppItemAttrVO
from alipay.aop.api.domain.PhoneStructVO import PhoneStructVO
from alipay.aop.api.domain.LocalItemSkuQueryVO import LocalItemSkuQueryVO
from alipay.aop.api.domain.TimeRangeStructVO import TimeRangeStructVO


class LocalItemVO(object):

    def __init__(self):
        self._attrs = None
        self._category_id = None
        self._customer_service_mobile = None
        self._head_img = None
        self._item_details_page_model = None
        self._item_id = None
        self._item_type = None
        self._merchant_name = None
        self._out_item_id = None
        self._path = None
        self._skus = None
        self._sold_time = None
        self._spu_status = None
        self._stock_num = None
        self._title = None

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        if isinstance(value, AppItemAttrVO):
            self._attrs = value
        else:
            self._attrs = AppItemAttrVO.from_alipay_dict(value)
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def customer_service_mobile(self):
        return self._customer_service_mobile

    @customer_service_mobile.setter
    def customer_service_mobile(self, value):
        if isinstance(value, PhoneStructVO):
            self._customer_service_mobile = value
        else:
            self._customer_service_mobile = PhoneStructVO.from_alipay_dict(value)
    @property
    def head_img(self):
        return self._head_img

    @head_img.setter
    def head_img(self, value):
        self._head_img = value
    @property
    def item_details_page_model(self):
        return self._item_details_page_model

    @item_details_page_model.setter
    def item_details_page_model(self, value):
        self._item_details_page_model = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
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
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, LocalItemSkuQueryVO):
                    self._skus.append(i)
                else:
                    self._skus.append(LocalItemSkuQueryVO.from_alipay_dict(i))
    @property
    def sold_time(self):
        return self._sold_time

    @sold_time.setter
    def sold_time(self, value):
        if isinstance(value, TimeRangeStructVO):
            self._sold_time = value
        else:
            self._sold_time = TimeRangeStructVO.from_alipay_dict(value)
    @property
    def spu_status(self):
        return self._spu_status

    @spu_status.setter
    def spu_status(self, value):
        self._spu_status = value
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
            if hasattr(self.attrs, 'to_alipay_dict'):
                params['attrs'] = self.attrs.to_alipay_dict()
            else:
                params['attrs'] = self.attrs
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.customer_service_mobile:
            if hasattr(self.customer_service_mobile, 'to_alipay_dict'):
                params['customer_service_mobile'] = self.customer_service_mobile.to_alipay_dict()
            else:
                params['customer_service_mobile'] = self.customer_service_mobile
        if self.head_img:
            if hasattr(self.head_img, 'to_alipay_dict'):
                params['head_img'] = self.head_img.to_alipay_dict()
            else:
                params['head_img'] = self.head_img
        if self.item_details_page_model:
            if hasattr(self.item_details_page_model, 'to_alipay_dict'):
                params['item_details_page_model'] = self.item_details_page_model.to_alipay_dict()
            else:
                params['item_details_page_model'] = self.item_details_page_model
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
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
        if self.sold_time:
            if hasattr(self.sold_time, 'to_alipay_dict'):
                params['sold_time'] = self.sold_time.to_alipay_dict()
            else:
                params['sold_time'] = self.sold_time
        if self.spu_status:
            if hasattr(self.spu_status, 'to_alipay_dict'):
                params['spu_status'] = self.spu_status.to_alipay_dict()
            else:
                params['spu_status'] = self.spu_status
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
        o = LocalItemVO()
        if 'attrs' in d:
            o.attrs = d['attrs']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'customer_service_mobile' in d:
            o.customer_service_mobile = d['customer_service_mobile']
        if 'head_img' in d:
            o.head_img = d['head_img']
        if 'item_details_page_model' in d:
            o.item_details_page_model = d['item_details_page_model']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'path' in d:
            o.path = d['path']
        if 'skus' in d:
            o.skus = d['skus']
        if 'sold_time' in d:
            o.sold_time = d['sold_time']
        if 'spu_status' in d:
            o.spu_status = d['spu_status']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        if 'title' in d:
            o.title = d['title']
        return o


