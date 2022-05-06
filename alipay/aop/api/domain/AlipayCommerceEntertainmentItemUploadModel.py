#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEntertainmentItemUploadModel(object):

    def __init__(self):
        self._enable = None
        self._item_extended_info = None
        self._item_id = None
        self._item_name = None
        self._item_url = None
        self._pic_source_url = None
        self._pricing_type = None
        self._service_category = None
        self._unit_price = None

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def item_extended_info(self):
        return self._item_extended_info

    @item_extended_info.setter
    def item_extended_info(self, value):
        self._item_extended_info = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_url(self):
        return self._item_url

    @item_url.setter
    def item_url(self, value):
        self._item_url = value
    @property
    def pic_source_url(self):
        return self._pic_source_url

    @pic_source_url.setter
    def pic_source_url(self, value):
        self._pic_source_url = value
    @property
    def pricing_type(self):
        return self._pricing_type

    @pricing_type.setter
    def pricing_type(self, value):
        self._pricing_type = value
    @property
    def service_category(self):
        return self._service_category

    @service_category.setter
    def service_category(self, value):
        self._service_category = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.enable:
            if hasattr(self.enable, 'to_alipay_dict'):
                params['enable'] = self.enable.to_alipay_dict()
            else:
                params['enable'] = self.enable
        if self.item_extended_info:
            if hasattr(self.item_extended_info, 'to_alipay_dict'):
                params['item_extended_info'] = self.item_extended_info.to_alipay_dict()
            else:
                params['item_extended_info'] = self.item_extended_info
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_url:
            if hasattr(self.item_url, 'to_alipay_dict'):
                params['item_url'] = self.item_url.to_alipay_dict()
            else:
                params['item_url'] = self.item_url
        if self.pic_source_url:
            if hasattr(self.pic_source_url, 'to_alipay_dict'):
                params['pic_source_url'] = self.pic_source_url.to_alipay_dict()
            else:
                params['pic_source_url'] = self.pic_source_url
        if self.pricing_type:
            if hasattr(self.pricing_type, 'to_alipay_dict'):
                params['pricing_type'] = self.pricing_type.to_alipay_dict()
            else:
                params['pricing_type'] = self.pricing_type
        if self.service_category:
            if hasattr(self.service_category, 'to_alipay_dict'):
                params['service_category'] = self.service_category.to_alipay_dict()
            else:
                params['service_category'] = self.service_category
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEntertainmentItemUploadModel()
        if 'enable' in d:
            o.enable = d['enable']
        if 'item_extended_info' in d:
            o.item_extended_info = d['item_extended_info']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_url' in d:
            o.item_url = d['item_url']
        if 'pic_source_url' in d:
            o.pic_source_url = d['pic_source_url']
        if 'pricing_type' in d:
            o.pricing_type = d['pricing_type']
        if 'service_category' in d:
            o.service_category = d['service_category']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


