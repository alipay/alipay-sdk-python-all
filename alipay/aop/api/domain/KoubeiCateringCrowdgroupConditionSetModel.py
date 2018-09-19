#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConditionItemPattern import ConditionItemPattern


class KoubeiCateringCrowdgroupConditionSetModel(object):

    def __init__(self):
        self._condition_model_list = None
        self._crowd_group_id = None
        self._describe = None
        self._operation = None
        self._operator_id = None
        self._operator_type = None
        self._shop_id = None

    @property
    def condition_model_list(self):
        return self._condition_model_list

    @condition_model_list.setter
    def condition_model_list(self, value):
        if isinstance(value, list):
            self._condition_model_list = list()
            for i in value:
                if isinstance(i, ConditionItemPattern):
                    self._condition_model_list.append(i)
                else:
                    self._condition_model_list.append(ConditionItemPattern.from_alipay_dict(i))
    @property
    def crowd_group_id(self):
        return self._crowd_group_id

    @crowd_group_id.setter
    def crowd_group_id(self, value):
        self._crowd_group_id = value
    @property
    def describe(self):
        return self._describe

    @describe.setter
    def describe(self, value):
        self._describe = value
    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.condition_model_list:
            if isinstance(self.condition_model_list, list):
                for i in range(0, len(self.condition_model_list)):
                    element = self.condition_model_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.condition_model_list[i] = element.to_alipay_dict()
            if hasattr(self.condition_model_list, 'to_alipay_dict'):
                params['condition_model_list'] = self.condition_model_list.to_alipay_dict()
            else:
                params['condition_model_list'] = self.condition_model_list
        if self.crowd_group_id:
            if hasattr(self.crowd_group_id, 'to_alipay_dict'):
                params['crowd_group_id'] = self.crowd_group_id.to_alipay_dict()
            else:
                params['crowd_group_id'] = self.crowd_group_id
        if self.describe:
            if hasattr(self.describe, 'to_alipay_dict'):
                params['describe'] = self.describe.to_alipay_dict()
            else:
                params['describe'] = self.describe
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringCrowdgroupConditionSetModel()
        if 'condition_model_list' in d:
            o.condition_model_list = d['condition_model_list']
        if 'crowd_group_id' in d:
            o.crowd_group_id = d['crowd_group_id']
        if 'describe' in d:
            o.describe = d['describe']
        if 'operation' in d:
            o.operation = d['operation']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


