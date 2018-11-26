#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MeterOpenModel import MeterOpenModel


class ExerciseItemOpenModelThird(object):

    def __init__(self):
        self._desc = None
        self._external_item_id = None
        self._item_code = None
        self._meter_list = None
        self._name = None
        self._parent_item_code = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def external_item_id(self):
        return self._external_item_id

    @external_item_id.setter
    def external_item_id(self, value):
        self._external_item_id = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def meter_list(self):
        return self._meter_list

    @meter_list.setter
    def meter_list(self, value):
        if isinstance(value, MeterOpenModel):
            self._meter_list = value
        else:
            self._meter_list = MeterOpenModel.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def parent_item_code(self):
        return self._parent_item_code

    @parent_item_code.setter
    def parent_item_code(self, value):
        self._parent_item_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.external_item_id:
            if hasattr(self.external_item_id, 'to_alipay_dict'):
                params['external_item_id'] = self.external_item_id.to_alipay_dict()
            else:
                params['external_item_id'] = self.external_item_id
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.meter_list:
            if hasattr(self.meter_list, 'to_alipay_dict'):
                params['meter_list'] = self.meter_list.to_alipay_dict()
            else:
                params['meter_list'] = self.meter_list
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.parent_item_code:
            if hasattr(self.parent_item_code, 'to_alipay_dict'):
                params['parent_item_code'] = self.parent_item_code.to_alipay_dict()
            else:
                params['parent_item_code'] = self.parent_item_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExerciseItemOpenModelThird()
        if 'desc' in d:
            o.desc = d['desc']
        if 'external_item_id' in d:
            o.external_item_id = d['external_item_id']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'meter_list' in d:
            o.meter_list = d['meter_list']
        if 'name' in d:
            o.name = d['name']
        if 'parent_item_code' in d:
            o.parent_item_code = d['parent_item_code']
        return o


