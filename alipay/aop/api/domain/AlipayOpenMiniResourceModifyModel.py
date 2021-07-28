#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniResourceRule import MiniResourceRule


class AlipayOpenMiniResourceModifyModel(object):

    def __init__(self):
        self._name = None
        self._resource_id = None
        self._row_num = None
        self._rule_list = None
        self._show_num = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def row_num(self):
        return self._row_num

    @row_num.setter
    def row_num(self, value):
        self._row_num = value
    @property
    def rule_list(self):
        return self._rule_list

    @rule_list.setter
    def rule_list(self, value):
        if isinstance(value, list):
            self._rule_list = list()
            for i in value:
                if isinstance(i, MiniResourceRule):
                    self._rule_list.append(i)
                else:
                    self._rule_list.append(MiniResourceRule.from_alipay_dict(i))
    @property
    def show_num(self):
        return self._show_num

    @show_num.setter
    def show_num(self, value):
        self._show_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        if self.row_num:
            if hasattr(self.row_num, 'to_alipay_dict'):
                params['row_num'] = self.row_num.to_alipay_dict()
            else:
                params['row_num'] = self.row_num
        if self.rule_list:
            if isinstance(self.rule_list, list):
                for i in range(0, len(self.rule_list)):
                    element = self.rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rule_list[i] = element.to_alipay_dict()
            if hasattr(self.rule_list, 'to_alipay_dict'):
                params['rule_list'] = self.rule_list.to_alipay_dict()
            else:
                params['rule_list'] = self.rule_list
        if self.show_num:
            if hasattr(self.show_num, 'to_alipay_dict'):
                params['show_num'] = self.show_num.to_alipay_dict()
            else:
                params['show_num'] = self.show_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniResourceModifyModel()
        if 'name' in d:
            o.name = d['name']
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        if 'row_num' in d:
            o.row_num = d['row_num']
        if 'rule_list' in d:
            o.rule_list = d['rule_list']
        if 'show_num' in d:
            o.show_num = d['show_num']
        return o


