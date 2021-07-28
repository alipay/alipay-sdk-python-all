#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishGroupSimplifyInfo import KbdishGroupSimplifyInfo
from alipay.aop.api.domain.KbdishMaterialSimplifyInfo import KbdishMaterialSimplifyInfo
from alipay.aop.api.domain.KbdishPropertySimplifyInfo import KbdishPropertySimplifyInfo
from alipay.aop.api.domain.KbdishSkuSimplifyInfo import KbdishSkuSimplifyInfo


class KbdishSimplyInfo(object):

    def __init__(self):
        self._add_remark = None
        self._catetory_name = None
        self._catetory_sort = None
        self._dish_name = None
        self._dmg_img = None
        self._group_list = None
        self._material_group_list = None
        self._min_serving = None
        self._out_dish_id = None
        self._out_shop_id = None
        self._property_list = None
        self._remarks = None
        self._shop_id = None
        self._sku_list = None
        self._status = None
        self._sub_name = None
        self._tags = None
        self._type_big = None
        self._unit = None

    @property
    def add_remark(self):
        return self._add_remark

    @add_remark.setter
    def add_remark(self, value):
        self._add_remark = value
    @property
    def catetory_name(self):
        return self._catetory_name

    @catetory_name.setter
    def catetory_name(self, value):
        self._catetory_name = value
    @property
    def catetory_sort(self):
        return self._catetory_sort

    @catetory_sort.setter
    def catetory_sort(self, value):
        self._catetory_sort = value
    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, value):
        self._dish_name = value
    @property
    def dmg_img(self):
        return self._dmg_img

    @dmg_img.setter
    def dmg_img(self, value):
        self._dmg_img = value
    @property
    def group_list(self):
        return self._group_list

    @group_list.setter
    def group_list(self, value):
        if isinstance(value, list):
            self._group_list = list()
            for i in value:
                if isinstance(i, KbdishGroupSimplifyInfo):
                    self._group_list.append(i)
                else:
                    self._group_list.append(KbdishGroupSimplifyInfo.from_alipay_dict(i))
    @property
    def material_group_list(self):
        return self._material_group_list

    @material_group_list.setter
    def material_group_list(self, value):
        if isinstance(value, list):
            self._material_group_list = list()
            for i in value:
                if isinstance(i, KbdishMaterialSimplifyInfo):
                    self._material_group_list.append(i)
                else:
                    self._material_group_list.append(KbdishMaterialSimplifyInfo.from_alipay_dict(i))
    @property
    def min_serving(self):
        return self._min_serving

    @min_serving.setter
    def min_serving(self, value):
        self._min_serving = value
    @property
    def out_dish_id(self):
        return self._out_dish_id

    @out_dish_id.setter
    def out_dish_id(self, value):
        self._out_dish_id = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def property_list(self):
        return self._property_list

    @property_list.setter
    def property_list(self, value):
        if isinstance(value, list):
            self._property_list = list()
            for i in value:
                if isinstance(i, KbdishPropertySimplifyInfo):
                    self._property_list.append(i)
                else:
                    self._property_list.append(KbdishPropertySimplifyInfo.from_alipay_dict(i))
    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, KbdishSkuSimplifyInfo):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(KbdishSkuSimplifyInfo.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_name(self):
        return self._sub_name

    @sub_name.setter
    def sub_name(self, value):
        self._sub_name = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value
    @property
    def type_big(self):
        return self._type_big

    @type_big.setter
    def type_big(self, value):
        self._type_big = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_remark:
            if hasattr(self.add_remark, 'to_alipay_dict'):
                params['add_remark'] = self.add_remark.to_alipay_dict()
            else:
                params['add_remark'] = self.add_remark
        if self.catetory_name:
            if hasattr(self.catetory_name, 'to_alipay_dict'):
                params['catetory_name'] = self.catetory_name.to_alipay_dict()
            else:
                params['catetory_name'] = self.catetory_name
        if self.catetory_sort:
            if hasattr(self.catetory_sort, 'to_alipay_dict'):
                params['catetory_sort'] = self.catetory_sort.to_alipay_dict()
            else:
                params['catetory_sort'] = self.catetory_sort
        if self.dish_name:
            if hasattr(self.dish_name, 'to_alipay_dict'):
                params['dish_name'] = self.dish_name.to_alipay_dict()
            else:
                params['dish_name'] = self.dish_name
        if self.dmg_img:
            if hasattr(self.dmg_img, 'to_alipay_dict'):
                params['dmg_img'] = self.dmg_img.to_alipay_dict()
            else:
                params['dmg_img'] = self.dmg_img
        if self.group_list:
            if isinstance(self.group_list, list):
                for i in range(0, len(self.group_list)):
                    element = self.group_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_list[i] = element.to_alipay_dict()
            if hasattr(self.group_list, 'to_alipay_dict'):
                params['group_list'] = self.group_list.to_alipay_dict()
            else:
                params['group_list'] = self.group_list
        if self.material_group_list:
            if isinstance(self.material_group_list, list):
                for i in range(0, len(self.material_group_list)):
                    element = self.material_group_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_group_list[i] = element.to_alipay_dict()
            if hasattr(self.material_group_list, 'to_alipay_dict'):
                params['material_group_list'] = self.material_group_list.to_alipay_dict()
            else:
                params['material_group_list'] = self.material_group_list
        if self.min_serving:
            if hasattr(self.min_serving, 'to_alipay_dict'):
                params['min_serving'] = self.min_serving.to_alipay_dict()
            else:
                params['min_serving'] = self.min_serving
        if self.out_dish_id:
            if hasattr(self.out_dish_id, 'to_alipay_dict'):
                params['out_dish_id'] = self.out_dish_id.to_alipay_dict()
            else:
                params['out_dish_id'] = self.out_dish_id
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
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
        if self.remarks:
            if hasattr(self.remarks, 'to_alipay_dict'):
                params['remarks'] = self.remarks.to_alipay_dict()
            else:
                params['remarks'] = self.remarks
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
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
        if self.sub_name:
            if hasattr(self.sub_name, 'to_alipay_dict'):
                params['sub_name'] = self.sub_name.to_alipay_dict()
            else:
                params['sub_name'] = self.sub_name
        if self.tags:
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.type_big:
            if hasattr(self.type_big, 'to_alipay_dict'):
                params['type_big'] = self.type_big.to_alipay_dict()
            else:
                params['type_big'] = self.type_big
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishSimplyInfo()
        if 'add_remark' in d:
            o.add_remark = d['add_remark']
        if 'catetory_name' in d:
            o.catetory_name = d['catetory_name']
        if 'catetory_sort' in d:
            o.catetory_sort = d['catetory_sort']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'dmg_img' in d:
            o.dmg_img = d['dmg_img']
        if 'group_list' in d:
            o.group_list = d['group_list']
        if 'material_group_list' in d:
            o.material_group_list = d['material_group_list']
        if 'min_serving' in d:
            o.min_serving = d['min_serving']
        if 'out_dish_id' in d:
            o.out_dish_id = d['out_dish_id']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'property_list' in d:
            o.property_list = d['property_list']
        if 'remarks' in d:
            o.remarks = d['remarks']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        if 'status' in d:
            o.status = d['status']
        if 'sub_name' in d:
            o.sub_name = d['sub_name']
        if 'tags' in d:
            o.tags = d['tags']
        if 'type_big' in d:
            o.type_big = d['type_big']
        if 'unit' in d:
            o.unit = d['unit']
        return o


