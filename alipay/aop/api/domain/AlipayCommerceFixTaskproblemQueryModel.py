#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceFixTaskproblemQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._item_id = None
        self._problem_level_1 = None
        self._problem_level_2 = None
        self._rule_scene = None
        self._scope = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def problem_level_1(self):
        return self._problem_level_1

    @problem_level_1.setter
    def problem_level_1(self, value):
        self._problem_level_1 = value
    @property
    def problem_level_2(self):
        return self._problem_level_2

    @problem_level_2.setter
    def problem_level_2(self, value):
        self._problem_level_2 = value
    @property
    def rule_scene(self):
        return self._rule_scene

    @rule_scene.setter
    def rule_scene(self, value):
        self._rule_scene = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.problem_level_1:
            if hasattr(self.problem_level_1, 'to_alipay_dict'):
                params['problem_level_1'] = self.problem_level_1.to_alipay_dict()
            else:
                params['problem_level_1'] = self.problem_level_1
        if self.problem_level_2:
            if hasattr(self.problem_level_2, 'to_alipay_dict'):
                params['problem_level_2'] = self.problem_level_2.to_alipay_dict()
            else:
                params['problem_level_2'] = self.problem_level_2
        if self.rule_scene:
            if hasattr(self.rule_scene, 'to_alipay_dict'):
                params['rule_scene'] = self.rule_scene.to_alipay_dict()
            else:
                params['rule_scene'] = self.rule_scene
        if self.scope:
            if hasattr(self.scope, 'to_alipay_dict'):
                params['scope'] = self.scope.to_alipay_dict()
            else:
                params['scope'] = self.scope
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceFixTaskproblemQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'problem_level_1' in d:
            o.problem_level_1 = d['problem_level_1']
        if 'problem_level_2' in d:
            o.problem_level_2 = d['problem_level_2']
        if 'rule_scene' in d:
            o.rule_scene = d['rule_scene']
        if 'scope' in d:
            o.scope = d['scope']
        return o


