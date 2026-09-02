#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupplyItemDTO(object):

    def __init__(self):
        self._default_supply = None
        self._instance_id = None
        self._plan_id = None
        self._style_type = None
        self._supply_id = None
        self._supply_name = None
        self._supply_type = None

    @property
    def default_supply(self):
        return self._default_supply

    @default_supply.setter
    def default_supply(self, value):
        self._default_supply = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def style_type(self):
        return self._style_type

    @style_type.setter
    def style_type(self, value):
        self._style_type = value
    @property
    def supply_id(self):
        return self._supply_id

    @supply_id.setter
    def supply_id(self, value):
        self._supply_id = value
    @property
    def supply_name(self):
        return self._supply_name

    @supply_name.setter
    def supply_name(self, value):
        self._supply_name = value
    @property
    def supply_type(self):
        return self._supply_type

    @supply_type.setter
    def supply_type(self, value):
        self._supply_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.default_supply:
            if hasattr(self.default_supply, 'to_alipay_dict'):
                params['default_supply'] = self.default_supply.to_alipay_dict()
            else:
                params['default_supply'] = self.default_supply
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.style_type:
            if hasattr(self.style_type, 'to_alipay_dict'):
                params['style_type'] = self.style_type.to_alipay_dict()
            else:
                params['style_type'] = self.style_type
        if self.supply_id:
            if hasattr(self.supply_id, 'to_alipay_dict'):
                params['supply_id'] = self.supply_id.to_alipay_dict()
            else:
                params['supply_id'] = self.supply_id
        if self.supply_name:
            if hasattr(self.supply_name, 'to_alipay_dict'):
                params['supply_name'] = self.supply_name.to_alipay_dict()
            else:
                params['supply_name'] = self.supply_name
        if self.supply_type:
            if hasattr(self.supply_type, 'to_alipay_dict'):
                params['supply_type'] = self.supply_type.to_alipay_dict()
            else:
                params['supply_type'] = self.supply_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupplyItemDTO()
        if 'default_supply' in d:
            o.default_supply = d['default_supply']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'style_type' in d:
            o.style_type = d['style_type']
        if 'supply_id' in d:
            o.supply_id = d['supply_id']
        if 'supply_name' in d:
            o.supply_name = d['supply_name']
        if 'supply_type' in d:
            o.supply_type = d['supply_type']
        return o


