#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CoreMaterialItemRelation import CoreMaterialItemRelation


class SupplierCoreMaterialInfo(object):

    def __init__(self):
        self._material_id = None
        self._material_name = None
        self._memo = None
        self._produce_period = None
        self._relation_item_list = None
        self._specs = None
        self._sub_type = None
        self._type = None

    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def material_name(self):
        return self._material_name

    @material_name.setter
    def material_name(self, value):
        self._material_name = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def produce_period(self):
        return self._produce_period

    @produce_period.setter
    def produce_period(self, value):
        self._produce_period = value
    @property
    def relation_item_list(self):
        return self._relation_item_list

    @relation_item_list.setter
    def relation_item_list(self, value):
        if isinstance(value, list):
            self._relation_item_list = list()
            for i in value:
                if isinstance(i, CoreMaterialItemRelation):
                    self._relation_item_list.append(i)
                else:
                    self._relation_item_list.append(CoreMaterialItemRelation.from_alipay_dict(i))
    @property
    def specs(self):
        return self._specs

    @specs.setter
    def specs(self, value):
        self._specs = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        if self.material_name:
            if hasattr(self.material_name, 'to_alipay_dict'):
                params['material_name'] = self.material_name.to_alipay_dict()
            else:
                params['material_name'] = self.material_name
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.produce_period:
            if hasattr(self.produce_period, 'to_alipay_dict'):
                params['produce_period'] = self.produce_period.to_alipay_dict()
            else:
                params['produce_period'] = self.produce_period
        if self.relation_item_list:
            if isinstance(self.relation_item_list, list):
                for i in range(0, len(self.relation_item_list)):
                    element = self.relation_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.relation_item_list[i] = element.to_alipay_dict()
            if hasattr(self.relation_item_list, 'to_alipay_dict'):
                params['relation_item_list'] = self.relation_item_list.to_alipay_dict()
            else:
                params['relation_item_list'] = self.relation_item_list
        if self.specs:
            if hasattr(self.specs, 'to_alipay_dict'):
                params['specs'] = self.specs.to_alipay_dict()
            else:
                params['specs'] = self.specs
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
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
        o = SupplierCoreMaterialInfo()
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'material_name' in d:
            o.material_name = d['material_name']
        if 'memo' in d:
            o.memo = d['memo']
        if 'produce_period' in d:
            o.produce_period = d['produce_period']
        if 'relation_item_list' in d:
            o.relation_item_list = d['relation_item_list']
        if 'specs' in d:
            o.specs = d['specs']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'type' in d:
            o.type = d['type']
        return o


