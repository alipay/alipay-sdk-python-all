#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MaterialModifyInfo import MaterialModifyInfo
from alipay.aop.api.domain.ItemPropertyInfo import ItemPropertyInfo
from alipay.aop.api.domain.SkuModifyInfo import SkuModifyInfo


class AntMerchantExpandItemSecurityModifyModel(object):

    def __init__(self):
        self._description = None
        self._front_category_id_list = None
        self._item_id = None
        self._material_list = None
        self._name = None
        self._property_list = None
        self._sku_list = None
        self._status = None
        self._type = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def front_category_id_list(self):
        return self._front_category_id_list

    @front_category_id_list.setter
    def front_category_id_list(self, value):
        if isinstance(value, list):
            self._front_category_id_list = list()
            for i in value:
                self._front_category_id_list.append(i)
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
                if isinstance(i, MaterialModifyInfo):
                    self._material_list.append(i)
                else:
                    self._material_list.append(MaterialModifyInfo.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def property_list(self):
        return self._property_list

    @property_list.setter
    def property_list(self, value):
        if isinstance(value, list):
            self._property_list = list()
            for i in value:
                if isinstance(i, ItemPropertyInfo):
                    self._property_list.append(i)
                else:
                    self._property_list.append(ItemPropertyInfo.from_alipay_dict(i))
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, SkuModifyInfo):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(SkuModifyInfo.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.front_category_id_list:
            if isinstance(self.front_category_id_list, list):
                for i in range(0, len(self.front_category_id_list)):
                    element = self.front_category_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.front_category_id_list[i] = element.to_alipay_dict()
            if hasattr(self.front_category_id_list, 'to_alipay_dict'):
                params['front_category_id_list'] = self.front_category_id_list.to_alipay_dict()
            else:
                params['front_category_id_list'] = self.front_category_id_list
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.property_list:
            if isinstance(self.property_list, list):
                for i in range(0, len(self.property_list)):
                    element = self.property_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property_list[i] = element.to_alipay_dict()
            if hasattr(self.property_list, 'to_alipay_dict'):
                params['property_list'] = self.property_list.to_alipay_dict()
            else:
                params['property_list'] = self.property_list
        if self.sku_list:
            if isinstance(self.sku_list, list):
                for i in range(0, len(self.sku_list)):
                    element = self.sku_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_list, 'to_alipay_dict'):
                params['sku_list'] = self.sku_list.to_alipay_dict()
            else:
                params['sku_list'] = self.sku_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandItemSecurityModifyModel()
        if 'description' in d:
            o.description = d['description']
        if 'front_category_id_list' in d:
            o.front_category_id_list = d['front_category_id_list']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'material_list' in d:
            o.material_list = d['material_list']
        if 'name' in d:
            o.name = d['name']
        if 'property_list' in d:
            o.property_list = d['property_list']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        return o


