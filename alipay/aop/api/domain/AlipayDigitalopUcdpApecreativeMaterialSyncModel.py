#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApeItemMaterial import ApeItemMaterial


class AlipayDigitalopUcdpApecreativeMaterialSyncModel(object):

    def __init__(self):
        self._create_type = None
        self._group_id = None
        self._group_name = None
        self._item_material_list = None
        self._project_id = None

    @property
    def create_type(self):
        return self._create_type

    @create_type.setter
    def create_type(self, value):
        self._create_type = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def item_material_list(self):
        return self._item_material_list

    @item_material_list.setter
    def item_material_list(self, value):
        if isinstance(value, list):
            self._item_material_list = list()
            for i in value:
                if isinstance(i, ApeItemMaterial):
                    self._item_material_list.append(i)
                else:
                    self._item_material_list.append(ApeItemMaterial.from_alipay_dict(i))
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_type:
            if hasattr(self.create_type, 'to_alipay_dict'):
                params['create_type'] = self.create_type.to_alipay_dict()
            else:
                params['create_type'] = self.create_type
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.item_material_list:
            if isinstance(self.item_material_list, list):
                for i in range(0, len(self.item_material_list)):
                    element = self.item_material_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_material_list[i] = element.to_alipay_dict()
            if hasattr(self.item_material_list, 'to_alipay_dict'):
                params['item_material_list'] = self.item_material_list.to_alipay_dict()
            else:
                params['item_material_list'] = self.item_material_list
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalopUcdpApecreativeMaterialSyncModel()
        if 'create_type' in d:
            o.create_type = d['create_type']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'item_material_list' in d:
            o.item_material_list = d['item_material_list']
        if 'project_id' in d:
            o.project_id = d['project_id']
        return o


