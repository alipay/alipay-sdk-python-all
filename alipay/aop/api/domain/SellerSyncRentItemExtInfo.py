#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SellerSyncRentItemExtInfo(object):

    def __init__(self):
        self._item_brand = None
        self._item_category = None
        self._item_color = None
        self._item_model = None
        self._item_name = None
        self._item_ram = None
        self._item_state = None
        self._provider_name = None
        self._purchasing_price = None
        self._serial_no = None

    @property
    def item_brand(self):
        return self._item_brand

    @item_brand.setter
    def item_brand(self, value):
        self._item_brand = value
    @property
    def item_category(self):
        return self._item_category

    @item_category.setter
    def item_category(self, value):
        self._item_category = value
    @property
    def item_color(self):
        return self._item_color

    @item_color.setter
    def item_color(self, value):
        self._item_color = value
    @property
    def item_model(self):
        return self._item_model

    @item_model.setter
    def item_model(self, value):
        self._item_model = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_ram(self):
        return self._item_ram

    @item_ram.setter
    def item_ram(self, value):
        self._item_ram = value
    @property
    def item_state(self):
        return self._item_state

    @item_state.setter
    def item_state(self, value):
        self._item_state = value
    @property
    def provider_name(self):
        return self._provider_name

    @provider_name.setter
    def provider_name(self, value):
        self._provider_name = value
    @property
    def purchasing_price(self):
        return self._purchasing_price

    @purchasing_price.setter
    def purchasing_price(self, value):
        self._purchasing_price = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_brand:
            if hasattr(self.item_brand, 'to_alipay_dict'):
                params['item_brand'] = self.item_brand.to_alipay_dict()
            else:
                params['item_brand'] = self.item_brand
        if self.item_category:
            if hasattr(self.item_category, 'to_alipay_dict'):
                params['item_category'] = self.item_category.to_alipay_dict()
            else:
                params['item_category'] = self.item_category
        if self.item_color:
            if hasattr(self.item_color, 'to_alipay_dict'):
                params['item_color'] = self.item_color.to_alipay_dict()
            else:
                params['item_color'] = self.item_color
        if self.item_model:
            if hasattr(self.item_model, 'to_alipay_dict'):
                params['item_model'] = self.item_model.to_alipay_dict()
            else:
                params['item_model'] = self.item_model
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_ram:
            if hasattr(self.item_ram, 'to_alipay_dict'):
                params['item_ram'] = self.item_ram.to_alipay_dict()
            else:
                params['item_ram'] = self.item_ram
        if self.item_state:
            if hasattr(self.item_state, 'to_alipay_dict'):
                params['item_state'] = self.item_state.to_alipay_dict()
            else:
                params['item_state'] = self.item_state
        if self.provider_name:
            if hasattr(self.provider_name, 'to_alipay_dict'):
                params['provider_name'] = self.provider_name.to_alipay_dict()
            else:
                params['provider_name'] = self.provider_name
        if self.purchasing_price:
            if hasattr(self.purchasing_price, 'to_alipay_dict'):
                params['purchasing_price'] = self.purchasing_price.to_alipay_dict()
            else:
                params['purchasing_price'] = self.purchasing_price
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SellerSyncRentItemExtInfo()
        if 'item_brand' in d:
            o.item_brand = d['item_brand']
        if 'item_category' in d:
            o.item_category = d['item_category']
        if 'item_color' in d:
            o.item_color = d['item_color']
        if 'item_model' in d:
            o.item_model = d['item_model']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_ram' in d:
            o.item_ram = d['item_ram']
        if 'item_state' in d:
            o.item_state = d['item_state']
        if 'provider_name' in d:
            o.provider_name = d['provider_name']
        if 'purchasing_price' in d:
            o.purchasing_price = d['purchasing_price']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        return o


