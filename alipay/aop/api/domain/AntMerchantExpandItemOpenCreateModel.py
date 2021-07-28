#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemExtInfo import ItemExtInfo
from alipay.aop.api.domain.MaterialCreateInfo import MaterialCreateInfo
from alipay.aop.api.domain.ItemPropertyInfo import ItemPropertyInfo
from alipay.aop.api.domain.SkuCreateInfo import SkuCreateInfo


class AntMerchantExpandItemOpenCreateModel(object):

    def __init__(self):
        self._description = None
        self._ext_info = None
        self._material_list = None
        self._name = None
        self._property_list = None
        self._scene = None
        self._sku_list = None
        self._standard_category_id = None
        self._target_id = None
        self._target_type = None
        self._type = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ItemExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ItemExtInfo.from_alipay_dict(i))
    @property
    def material_list(self):
        return self._material_list

    @material_list.setter
    def material_list(self, value):
        if isinstance(value, list):
            self._material_list = list()
            for i in value:
                if isinstance(i, MaterialCreateInfo):
                    self._material_list.append(i)
                else:
                    self._material_list.append(MaterialCreateInfo.from_alipay_dict(i))
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
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, SkuCreateInfo):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(SkuCreateInfo.from_alipay_dict(i))
    @property
    def standard_category_id(self):
        return self._standard_category_id

    @standard_category_id.setter
    def standard_category_id(self, value):
        self._standard_category_id = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value
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
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
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
        if self.standard_category_id:
            if hasattr(self.standard_category_id, 'to_alipay_dict'):
                params['standard_category_id'] = self.standard_category_id.to_alipay_dict()
            else:
                params['standard_category_id'] = self.standard_category_id
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_type:
            if hasattr(self.target_type, 'to_alipay_dict'):
                params['target_type'] = self.target_type.to_alipay_dict()
            else:
                params['target_type'] = self.target_type
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
        o = AntMerchantExpandItemOpenCreateModel()
        if 'description' in d:
            o.description = d['description']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'material_list' in d:
            o.material_list = d['material_list']
        if 'name' in d:
            o.name = d['name']
        if 'property_list' in d:
            o.property_list = d['property_list']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        if 'standard_category_id' in d:
            o.standard_category_id = d['standard_category_id']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_type' in d:
            o.target_type = d['target_type']
        if 'type' in d:
            o.type = d['type']
        return o


