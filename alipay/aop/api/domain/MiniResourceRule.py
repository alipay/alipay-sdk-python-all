#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniResourceRule(object):

    def __init__(self):
        self._floor_id = None
        self._identity_id = None
        self._identity_name = None
        self._item_id_list = None
        self._origin = None
        self._rule_id = None
        self._rule_name = None
        self._type = None

    @property
    def floor_id(self):
        return self._floor_id

    @floor_id.setter
    def floor_id(self, value):
        self._floor_id = value
    @property
    def identity_id(self):
        return self._identity_id

    @identity_id.setter
    def identity_id(self, value):
        self._identity_id = value
    @property
    def identity_name(self):
        return self._identity_name

    @identity_name.setter
    def identity_name(self, value):
        self._identity_name = value
    @property
    def item_id_list(self):
        return self._item_id_list

    @item_id_list.setter
    def item_id_list(self, value):
        self._item_id_list = value
    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.floor_id:
            if hasattr(self.floor_id, 'to_alipay_dict'):
                params['floor_id'] = self.floor_id.to_alipay_dict()
            else:
                params['floor_id'] = self.floor_id
        if self.identity_id:
            if hasattr(self.identity_id, 'to_alipay_dict'):
                params['identity_id'] = self.identity_id.to_alipay_dict()
            else:
                params['identity_id'] = self.identity_id
        if self.identity_name:
            if hasattr(self.identity_name, 'to_alipay_dict'):
                params['identity_name'] = self.identity_name.to_alipay_dict()
            else:
                params['identity_name'] = self.identity_name
        if self.item_id_list:
            if hasattr(self.item_id_list, 'to_alipay_dict'):
                params['item_id_list'] = self.item_id_list.to_alipay_dict()
            else:
                params['item_id_list'] = self.item_id_list
        if self.origin:
            if hasattr(self.origin, 'to_alipay_dict'):
                params['origin'] = self.origin.to_alipay_dict()
            else:
                params['origin'] = self.origin
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
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
        o = MiniResourceRule()
        if 'floor_id' in d:
            o.floor_id = d['floor_id']
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        if 'identity_name' in d:
            o.identity_name = d['identity_name']
        if 'item_id_list' in d:
            o.item_id_list = d['item_id_list']
        if 'origin' in d:
            o.origin = d['origin']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'type' in d:
            o.type = d['type']
        return o


