#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConditionItemPattern import ConditionItemPattern


class UserCrowdConditions(object):

    def __init__(self):
        self._crowd_group_id = None
        self._describe = None
        self._hit_crowd_conditons = None

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
    def hit_crowd_conditons(self):
        return self._hit_crowd_conditons

    @hit_crowd_conditons.setter
    def hit_crowd_conditons(self, value):
        if isinstance(value, list):
            self._hit_crowd_conditons = list()
            for i in value:
                if isinstance(i, ConditionItemPattern):
                    self._hit_crowd_conditons.append(i)
                else:
                    self._hit_crowd_conditons.append(ConditionItemPattern.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
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
        if self.hit_crowd_conditons:
            if isinstance(self.hit_crowd_conditons, list):
                for i in range(0, len(self.hit_crowd_conditons)):
                    element = self.hit_crowd_conditons[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hit_crowd_conditons[i] = element.to_alipay_dict()
            if hasattr(self.hit_crowd_conditons, 'to_alipay_dict'):
                params['hit_crowd_conditons'] = self.hit_crowd_conditons.to_alipay_dict()
            else:
                params['hit_crowd_conditons'] = self.hit_crowd_conditons
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserCrowdConditions()
        if 'crowd_group_id' in d:
            o.crowd_group_id = d['crowd_group_id']
        if 'describe' in d:
            o.describe = d['describe']
        if 'hit_crowd_conditons' in d:
            o.hit_crowd_conditons = d['hit_crowd_conditons']
        return o


