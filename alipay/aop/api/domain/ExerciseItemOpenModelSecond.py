#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExerciseItemOpenModelThird import ExerciseItemOpenModelThird
from alipay.aop.api.domain.MeterOpenModel import MeterOpenModel


class ExerciseItemOpenModelSecond(object):

    def __init__(self):
        self._desc = None
        self._external_item_id = None
        self._item_code = None
        self._item_list = None
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
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, ExerciseItemOpenModelThird):
                    self._item_list.append(i)
                else:
                    self._item_list.append(ExerciseItemOpenModelThird.from_alipay_dict(i))
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
        if self.item_list:
            if isinstance(self.item_list, list):
                for i in range(0, len(self.item_list)):
                    element = self.item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_list[i] = element.to_alipay_dict()
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
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
        o = ExerciseItemOpenModelSecond()
        if 'desc' in d:
            o.desc = d['desc']
        if 'external_item_id' in d:
            o.external_item_id = d['external_item_id']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'meter_list' in d:
            o.meter_list = d['meter_list']
        if 'name' in d:
            o.name = d['name']
        if 'parent_item_code' in d:
            o.parent_item_code = d['parent_item_code']
        return o


