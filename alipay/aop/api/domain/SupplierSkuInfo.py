#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SupplierItemAttrField import SupplierItemAttrField


class SupplierSkuInfo(object):

    def __init__(self):
        self._attr_collect = None
        self._bar_code = None
        self._batch_mgmt_flag = None
        self._brand_code = None
        self._brand_name = None
        self._category_id = None
        self._category_name = None
        self._fragile_flag = None
        self._hazardous_flag = None
        self._item_code = None
        self._item_name = None
        self._item_type = None
        self._liquid_flag = None
        self._lockup_lifecycle = None
        self._reject_lifecycle = None
        self._shelf_life = None
        self._shelf_life_mgmt_flag = None
        self._snmgmt_flag = None

    @property
    def attr_collect(self):
        return self._attr_collect

    @attr_collect.setter
    def attr_collect(self, value):
        if isinstance(value, list):
            self._attr_collect = list()
            for i in value:
                if isinstance(i, SupplierItemAttrField):
                    self._attr_collect.append(i)
                else:
                    self._attr_collect.append(SupplierItemAttrField.from_alipay_dict(i))
    @property
    def bar_code(self):
        return self._bar_code

    @bar_code.setter
    def bar_code(self, value):
        self._bar_code = value
    @property
    def batch_mgmt_flag(self):
        return self._batch_mgmt_flag

    @batch_mgmt_flag.setter
    def batch_mgmt_flag(self, value):
        self._batch_mgmt_flag = value
    @property
    def brand_code(self):
        return self._brand_code

    @brand_code.setter
    def brand_code(self, value):
        self._brand_code = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def fragile_flag(self):
        return self._fragile_flag

    @fragile_flag.setter
    def fragile_flag(self, value):
        self._fragile_flag = value
    @property
    def hazardous_flag(self):
        return self._hazardous_flag

    @hazardous_flag.setter
    def hazardous_flag(self, value):
        self._hazardous_flag = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def liquid_flag(self):
        return self._liquid_flag

    @liquid_flag.setter
    def liquid_flag(self, value):
        self._liquid_flag = value
    @property
    def lockup_lifecycle(self):
        return self._lockup_lifecycle

    @lockup_lifecycle.setter
    def lockup_lifecycle(self, value):
        self._lockup_lifecycle = value
    @property
    def reject_lifecycle(self):
        return self._reject_lifecycle

    @reject_lifecycle.setter
    def reject_lifecycle(self, value):
        self._reject_lifecycle = value
    @property
    def shelf_life(self):
        return self._shelf_life

    @shelf_life.setter
    def shelf_life(self, value):
        self._shelf_life = value
    @property
    def shelf_life_mgmt_flag(self):
        return self._shelf_life_mgmt_flag

    @shelf_life_mgmt_flag.setter
    def shelf_life_mgmt_flag(self, value):
        self._shelf_life_mgmt_flag = value
    @property
    def snmgmt_flag(self):
        return self._snmgmt_flag

    @snmgmt_flag.setter
    def snmgmt_flag(self, value):
        self._snmgmt_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_collect:
            if isinstance(self.attr_collect, list):
                for i in range(0, len(self.attr_collect)):
                    element = self.attr_collect[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attr_collect[i] = element.to_alipay_dict()
            if hasattr(self.attr_collect, 'to_alipay_dict'):
                params['attr_collect'] = self.attr_collect.to_alipay_dict()
            else:
                params['attr_collect'] = self.attr_collect
        if self.bar_code:
            if hasattr(self.bar_code, 'to_alipay_dict'):
                params['bar_code'] = self.bar_code.to_alipay_dict()
            else:
                params['bar_code'] = self.bar_code
        if self.batch_mgmt_flag:
            if hasattr(self.batch_mgmt_flag, 'to_alipay_dict'):
                params['batch_mgmt_flag'] = self.batch_mgmt_flag.to_alipay_dict()
            else:
                params['batch_mgmt_flag'] = self.batch_mgmt_flag
        if self.brand_code:
            if hasattr(self.brand_code, 'to_alipay_dict'):
                params['brand_code'] = self.brand_code.to_alipay_dict()
            else:
                params['brand_code'] = self.brand_code
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.fragile_flag:
            if hasattr(self.fragile_flag, 'to_alipay_dict'):
                params['fragile_flag'] = self.fragile_flag.to_alipay_dict()
            else:
                params['fragile_flag'] = self.fragile_flag
        if self.hazardous_flag:
            if hasattr(self.hazardous_flag, 'to_alipay_dict'):
                params['hazardous_flag'] = self.hazardous_flag.to_alipay_dict()
            else:
                params['hazardous_flag'] = self.hazardous_flag
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.liquid_flag:
            if hasattr(self.liquid_flag, 'to_alipay_dict'):
                params['liquid_flag'] = self.liquid_flag.to_alipay_dict()
            else:
                params['liquid_flag'] = self.liquid_flag
        if self.lockup_lifecycle:
            if hasattr(self.lockup_lifecycle, 'to_alipay_dict'):
                params['lockup_lifecycle'] = self.lockup_lifecycle.to_alipay_dict()
            else:
                params['lockup_lifecycle'] = self.lockup_lifecycle
        if self.reject_lifecycle:
            if hasattr(self.reject_lifecycle, 'to_alipay_dict'):
                params['reject_lifecycle'] = self.reject_lifecycle.to_alipay_dict()
            else:
                params['reject_lifecycle'] = self.reject_lifecycle
        if self.shelf_life:
            if hasattr(self.shelf_life, 'to_alipay_dict'):
                params['shelf_life'] = self.shelf_life.to_alipay_dict()
            else:
                params['shelf_life'] = self.shelf_life
        if self.shelf_life_mgmt_flag:
            if hasattr(self.shelf_life_mgmt_flag, 'to_alipay_dict'):
                params['shelf_life_mgmt_flag'] = self.shelf_life_mgmt_flag.to_alipay_dict()
            else:
                params['shelf_life_mgmt_flag'] = self.shelf_life_mgmt_flag
        if self.snmgmt_flag:
            if hasattr(self.snmgmt_flag, 'to_alipay_dict'):
                params['snmgmt_flag'] = self.snmgmt_flag.to_alipay_dict()
            else:
                params['snmgmt_flag'] = self.snmgmt_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupplierSkuInfo()
        if 'attr_collect' in d:
            o.attr_collect = d['attr_collect']
        if 'bar_code' in d:
            o.bar_code = d['bar_code']
        if 'batch_mgmt_flag' in d:
            o.batch_mgmt_flag = d['batch_mgmt_flag']
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'fragile_flag' in d:
            o.fragile_flag = d['fragile_flag']
        if 'hazardous_flag' in d:
            o.hazardous_flag = d['hazardous_flag']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'liquid_flag' in d:
            o.liquid_flag = d['liquid_flag']
        if 'lockup_lifecycle' in d:
            o.lockup_lifecycle = d['lockup_lifecycle']
        if 'reject_lifecycle' in d:
            o.reject_lifecycle = d['reject_lifecycle']
        if 'shelf_life' in d:
            o.shelf_life = d['shelf_life']
        if 'shelf_life_mgmt_flag' in d:
            o.shelf_life_mgmt_flag = d['shelf_life_mgmt_flag']
        if 'snmgmt_flag' in d:
            o.snmgmt_flag = d['snmgmt_flag']
        return o


