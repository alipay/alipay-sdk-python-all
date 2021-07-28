#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MaterialInfo import MaterialInfo
from alipay.aop.api.domain.ItemSkuPropertyInfo import ItemSkuPropertyInfo


class CmItemSkuInfo(object):

    def __init__(self):
        self._gmt_create = None
        self._gmt_modified = None
        self._inventory = None
        self._item_id = None
        self._material_list = None
        self._original_price = None
        self._price = None
        self._remain_inventory = None
        self._sku_id = None
        self._sku_property_list = None
        self._status = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def material_list(self):
        return self._material_list

    @material_list.setter
    def material_list(self, value):
        if isinstance(value, list):
            self._material_list = list()
            for i in value:
                if isinstance(i, MaterialInfo):
                    self._material_list.append(i)
                else:
                    self._material_list.append(MaterialInfo.from_alipay_dict(i))
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def remain_inventory(self):
        return self._remain_inventory

    @remain_inventory.setter
    def remain_inventory(self, value):
        self._remain_inventory = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_property_list(self):
        return self._sku_property_list

    @sku_property_list.setter
    def sku_property_list(self, value):
        if isinstance(value, list):
            self._sku_property_list = list()
            for i in value:
                if isinstance(i, ItemSkuPropertyInfo):
                    self._sku_property_list.append(i)
                else:
                    self._sku_property_list.append(ItemSkuPropertyInfo.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.material_list:
            if isinstance(self.material_list, list):
                for i in range(0, len(self.material_list)):
                    element = self.material_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_list[i] = element.to_alipay_dict()
            if hasattr(self.material_list, 'to_alipay_dict'):
                params['material_list'] = self.material_list.to_alipay_dict()
            else:
                params['material_list'] = self.material_list
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.remain_inventory:
            if hasattr(self.remain_inventory, 'to_alipay_dict'):
                params['remain_inventory'] = self.remain_inventory.to_alipay_dict()
            else:
                params['remain_inventory'] = self.remain_inventory
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_property_list:
            if isinstance(self.sku_property_list, list):
                for i in range(0, len(self.sku_property_list)):
                    element = self.sku_property_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_property_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_property_list, 'to_alipay_dict'):
                params['sku_property_list'] = self.sku_property_list.to_alipay_dict()
            else:
                params['sku_property_list'] = self.sku_property_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CmItemSkuInfo()
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'material_list' in d:
            o.material_list = d['material_list']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'price' in d:
            o.price = d['price']
        if 'remain_inventory' in d:
            o.remain_inventory = d['remain_inventory']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_property_list' in d:
            o.sku_property_list = d['sku_property_list']
        if 'status' in d:
            o.status = d['status']
        return o


