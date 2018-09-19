#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Position import Position


class AdGroup(object):

    def __init__(self):
        self._ad_user_id = None
        self._crowd_condition = None
        self._group_id = None
        self._group_name = None
        self._plan_id = None
        self._position_condition = None
        self._quantity = None

    @property
    def ad_user_id(self):
        return self._ad_user_id

    @ad_user_id.setter
    def ad_user_id(self, value):
        self._ad_user_id = value
    @property
    def crowd_condition(self):
        return self._crowd_condition

    @crowd_condition.setter
    def crowd_condition(self, value):
        self._crowd_condition = value
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
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def position_condition(self):
        return self._position_condition

    @position_condition.setter
    def position_condition(self, value):
        if isinstance(value, list):
            self._position_condition = list()
            for i in value:
                if isinstance(i, Position):
                    self._position_condition.append(i)
                else:
                    self._position_condition.append(Position.from_alipay_dict(i))
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_user_id:
            if hasattr(self.ad_user_id, 'to_alipay_dict'):
                params['ad_user_id'] = self.ad_user_id.to_alipay_dict()
            else:
                params['ad_user_id'] = self.ad_user_id
        if self.crowd_condition:
            if hasattr(self.crowd_condition, 'to_alipay_dict'):
                params['crowd_condition'] = self.crowd_condition.to_alipay_dict()
            else:
                params['crowd_condition'] = self.crowd_condition
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
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.position_condition:
            if isinstance(self.position_condition, list):
                for i in range(0, len(self.position_condition)):
                    element = self.position_condition[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.position_condition[i] = element.to_alipay_dict()
            if hasattr(self.position_condition, 'to_alipay_dict'):
                params['position_condition'] = self.position_condition.to_alipay_dict()
            else:
                params['position_condition'] = self.position_condition
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdGroup()
        if 'ad_user_id' in d:
            o.ad_user_id = d['ad_user_id']
        if 'crowd_condition' in d:
            o.crowd_condition = d['crowd_condition']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'position_condition' in d:
            o.position_condition = d['position_condition']
        if 'quantity' in d:
            o.quantity = d['quantity']
        return o


