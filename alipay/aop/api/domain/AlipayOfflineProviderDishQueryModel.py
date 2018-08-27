#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderDishQueryModel(object):

    def __init__(self):
        self._dish_type_name = None
        self._order_by = None
        self._outer_dish_id = None
        self._page = None
        self._page_size = None
        self._shop_id = None

    @property
    def dish_type_name(self):
        return self._dish_type_name

    @dish_type_name.setter
    def dish_type_name(self, value):
        self._dish_type_name = value
    @property
    def order_by(self):
        return self._order_by

    @order_by.setter
    def order_by(self, value):
        self._order_by = value
    @property
    def outer_dish_id(self):
        return self._outer_dish_id

    @outer_dish_id.setter
    def outer_dish_id(self, value):
        self._outer_dish_id = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.dish_type_name:
            if hasattr(self.dish_type_name, 'to_alipay_dict'):
                params['dish_type_name'] = self.dish_type_name.to_alipay_dict()
            else:
                params['dish_type_name'] = self.dish_type_name
        if self.order_by:
            if hasattr(self.order_by, 'to_alipay_dict'):
                params['order_by'] = self.order_by.to_alipay_dict()
            else:
                params['order_by'] = self.order_by
        if self.outer_dish_id:
            if hasattr(self.outer_dish_id, 'to_alipay_dict'):
                params['outer_dish_id'] = self.outer_dish_id.to_alipay_dict()
            else:
                params['outer_dish_id'] = self.outer_dish_id
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderDishQueryModel()
        if 'dish_type_name' in d:
            o.dish_type_name = d['dish_type_name']
        if 'order_by' in d:
            o.order_by = d['order_by']
        if 'outer_dish_id' in d:
            o.outer_dish_id = d['outer_dish_id']
        if 'page' in d:
            o.page = d['page']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


