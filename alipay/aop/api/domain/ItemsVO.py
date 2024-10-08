#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemsVO(object):

    def __init__(self):
        self._amount_item = None
        self._app_item_code = None
        self._is_mi_item = None
        self._item_name = None
        self._price_original = None
        self._price_sale = None
        self._quantity_item = None
        self._shelf_code = None
        self._sku_id = None
        self._upc = None
        self._weight_item = None
        self._weight_unit = None

    @property
    def amount_item(self):
        return self._amount_item

    @amount_item.setter
    def amount_item(self, value):
        self._amount_item = value
    @property
    def app_item_code(self):
        return self._app_item_code

    @app_item_code.setter
    def app_item_code(self, value):
        self._app_item_code = value
    @property
    def is_mi_item(self):
        return self._is_mi_item

    @is_mi_item.setter
    def is_mi_item(self, value):
        self._is_mi_item = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def price_original(self):
        return self._price_original

    @price_original.setter
    def price_original(self, value):
        self._price_original = value
    @property
    def price_sale(self):
        return self._price_sale

    @price_sale.setter
    def price_sale(self, value):
        self._price_sale = value
    @property
    def quantity_item(self):
        return self._quantity_item

    @quantity_item.setter
    def quantity_item(self, value):
        self._quantity_item = value
    @property
    def shelf_code(self):
        return self._shelf_code

    @shelf_code.setter
    def shelf_code(self, value):
        self._shelf_code = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def upc(self):
        return self._upc

    @upc.setter
    def upc(self, value):
        self._upc = value
    @property
    def weight_item(self):
        return self._weight_item

    @weight_item.setter
    def weight_item(self, value):
        self._weight_item = value
    @property
    def weight_unit(self):
        return self._weight_unit

    @weight_unit.setter
    def weight_unit(self, value):
        self._weight_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_item:
            if hasattr(self.amount_item, 'to_alipay_dict'):
                params['amount_item'] = self.amount_item.to_alipay_dict()
            else:
                params['amount_item'] = self.amount_item
        if self.app_item_code:
            if hasattr(self.app_item_code, 'to_alipay_dict'):
                params['app_item_code'] = self.app_item_code.to_alipay_dict()
            else:
                params['app_item_code'] = self.app_item_code
        if self.is_mi_item:
            if hasattr(self.is_mi_item, 'to_alipay_dict'):
                params['is_mi_item'] = self.is_mi_item.to_alipay_dict()
            else:
                params['is_mi_item'] = self.is_mi_item
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.price_original:
            if hasattr(self.price_original, 'to_alipay_dict'):
                params['price_original'] = self.price_original.to_alipay_dict()
            else:
                params['price_original'] = self.price_original
        if self.price_sale:
            if hasattr(self.price_sale, 'to_alipay_dict'):
                params['price_sale'] = self.price_sale.to_alipay_dict()
            else:
                params['price_sale'] = self.price_sale
        if self.quantity_item:
            if hasattr(self.quantity_item, 'to_alipay_dict'):
                params['quantity_item'] = self.quantity_item.to_alipay_dict()
            else:
                params['quantity_item'] = self.quantity_item
        if self.shelf_code:
            if hasattr(self.shelf_code, 'to_alipay_dict'):
                params['shelf_code'] = self.shelf_code.to_alipay_dict()
            else:
                params['shelf_code'] = self.shelf_code
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.upc:
            if hasattr(self.upc, 'to_alipay_dict'):
                params['upc'] = self.upc.to_alipay_dict()
            else:
                params['upc'] = self.upc
        if self.weight_item:
            if hasattr(self.weight_item, 'to_alipay_dict'):
                params['weight_item'] = self.weight_item.to_alipay_dict()
            else:
                params['weight_item'] = self.weight_item
        if self.weight_unit:
            if hasattr(self.weight_unit, 'to_alipay_dict'):
                params['weight_unit'] = self.weight_unit.to_alipay_dict()
            else:
                params['weight_unit'] = self.weight_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemsVO()
        if 'amount_item' in d:
            o.amount_item = d['amount_item']
        if 'app_item_code' in d:
            o.app_item_code = d['app_item_code']
        if 'is_mi_item' in d:
            o.is_mi_item = d['is_mi_item']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'price_original' in d:
            o.price_original = d['price_original']
        if 'price_sale' in d:
            o.price_sale = d['price_sale']
        if 'quantity_item' in d:
            o.quantity_item = d['quantity_item']
        if 'shelf_code' in d:
            o.shelf_code = d['shelf_code']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'upc' in d:
            o.upc = d['upc']
        if 'weight_item' in d:
            o.weight_item = d['weight_item']
        if 'weight_unit' in d:
            o.weight_unit = d['weight_unit']
        return o


