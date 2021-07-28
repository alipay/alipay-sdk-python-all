#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishBaseActivityInfo import KbdishBaseActivityInfo
from alipay.aop.api.domain.KbdishGroupSimplifyInfo import KbdishGroupSimplifyInfo
from alipay.aop.api.domain.KbdishMaterialSimplifyInfo import KbdishMaterialSimplifyInfo
from alipay.aop.api.domain.KbdishPeriodExtendInfo import KbdishPeriodExtendInfo
from alipay.aop.api.domain.KbdishPropertySimplifyInfo import KbdishPropertySimplifyInfo
from alipay.aop.api.domain.KbdishSkuSimplifyInfo import KbdishSkuSimplifyInfo


class KoubeiCateringDishCreatedishSyncModel(object):

    def __init__(self):
        self._activity_info = None
        self._catetory_name = None
        self._catetory_sort = None
        self._dish_background_img = None
        self._dish_detail_img_list = None
        self._dmg_img = None
        self._group_list = None
        self._material_group_list = None
        self._min_serving = None
        self._name = None
        self._non_whole_order_discount = None
        self._out_dish_id = None
        self._out_shop_id = None
        self._period = None
        self._property_list = None
        self._remarks = None
        self._shop_id = None
        self._sku_list = None
        self._status = None
        self._sub_name = None
        self._tags = None
        self._type_big = None
        self._type_sub = None
        self._unit = None

    @property
    def activity_info(self):
        return self._activity_info

    @activity_info.setter
    def activity_info(self, value):
        if isinstance(value, KbdishBaseActivityInfo):
            self._activity_info = value
        else:
            self._activity_info = KbdishBaseActivityInfo.from_alipay_dict(value)
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
    def dish_background_img(self):
        return self._dish_background_img

    @dish_background_img.setter
    def dish_background_img(self, value):
        self._dish_background_img = value
    @property
    def dish_detail_img_list(self):
        return self._dish_detail_img_list

    @dish_detail_img_list.setter
    def dish_detail_img_list(self, value):
        if isinstance(value, list):
            self._dish_detail_img_list = list()
            for i in value:
                self._dish_detail_img_list.append(i)
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def non_whole_order_discount(self):
        return self._non_whole_order_discount

    @non_whole_order_discount.setter
    def non_whole_order_discount(self, value):
        self._non_whole_order_discount = value
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
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        if isinstance(value, KbdishPeriodExtendInfo):
            self._period = value
        else:
            self._period = KbdishPeriodExtendInfo.from_alipay_dict(value)
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
    def type_sub(self):
        return self._type_sub

    @type_sub.setter
    def type_sub(self, value):
        self._type_sub = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_info:
            if hasattr(self.activity_info, 'to_alipay_dict'):
                params['activity_info'] = self.activity_info.to_alipay_dict()
            else:
                params['activity_info'] = self.activity_info
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
        if self.dish_background_img:
            if hasattr(self.dish_background_img, 'to_alipay_dict'):
                params['dish_background_img'] = self.dish_background_img.to_alipay_dict()
            else:
                params['dish_background_img'] = self.dish_background_img
        if self.dish_detail_img_list:
            if isinstance(self.dish_detail_img_list, list):
                for i in range(0, len(self.dish_detail_img_list)):
                    element = self.dish_detail_img_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_detail_img_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_detail_img_list, 'to_alipay_dict'):
                params['dish_detail_img_list'] = self.dish_detail_img_list.to_alipay_dict()
            else:
                params['dish_detail_img_list'] = self.dish_detail_img_list
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.non_whole_order_discount:
            if hasattr(self.non_whole_order_discount, 'to_alipay_dict'):
                params['non_whole_order_discount'] = self.non_whole_order_discount.to_alipay_dict()
            else:
                params['non_whole_order_discount'] = self.non_whole_order_discount
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
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
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
        if self.type_sub:
            if hasattr(self.type_sub, 'to_alipay_dict'):
                params['type_sub'] = self.type_sub.to_alipay_dict()
            else:
                params['type_sub'] = self.type_sub
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
        o = KoubeiCateringDishCreatedishSyncModel()
        if 'activity_info' in d:
            o.activity_info = d['activity_info']
        if 'catetory_name' in d:
            o.catetory_name = d['catetory_name']
        if 'catetory_sort' in d:
            o.catetory_sort = d['catetory_sort']
        if 'dish_background_img' in d:
            o.dish_background_img = d['dish_background_img']
        if 'dish_detail_img_list' in d:
            o.dish_detail_img_list = d['dish_detail_img_list']
        if 'dmg_img' in d:
            o.dmg_img = d['dmg_img']
        if 'group_list' in d:
            o.group_list = d['group_list']
        if 'material_group_list' in d:
            o.material_group_list = d['material_group_list']
        if 'min_serving' in d:
            o.min_serving = d['min_serving']
        if 'name' in d:
            o.name = d['name']
        if 'non_whole_order_discount' in d:
            o.non_whole_order_discount = d['non_whole_order_discount']
        if 'out_dish_id' in d:
            o.out_dish_id = d['out_dish_id']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'period' in d:
            o.period = d['period']
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
        if 'type_sub' in d:
            o.type_sub = d['type_sub']
        if 'unit' in d:
            o.unit = d['unit']
        return o


