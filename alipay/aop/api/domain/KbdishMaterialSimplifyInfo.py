#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishMaterialSimplifyInfo(object):

    def __init__(self):
        self._material_detail_list = None
        self._material_rule = None
        self._name = None

    @property
    def material_detail_list(self):
        return self._material_detail_list

    @material_detail_list.setter
    def material_detail_list(self, value):
        if isinstance(value, list):
            self._material_detail_list = list()
            for i in value:
                self._material_detail_list.append(i)
    @property
    def material_rule(self):
        return self._material_rule

    @material_rule.setter
    def material_rule(self, value):
        self._material_rule = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.material_detail_list:
            if isinstance(self.material_detail_list, list):
                for i in range(0, len(self.material_detail_list)):
                    element = self.material_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.material_detail_list, 'to_alipay_dict'):
                params['material_detail_list'] = self.material_detail_list.to_alipay_dict()
            else:
                params['material_detail_list'] = self.material_detail_list
        if self.material_rule:
            if hasattr(self.material_rule, 'to_alipay_dict'):
                params['material_rule'] = self.material_rule.to_alipay_dict()
            else:
                params['material_rule'] = self.material_rule
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishMaterialSimplifyInfo()
        if 'material_detail_list' in d:
            o.material_detail_list = d['material_detail_list']
        if 'material_rule' in d:
            o.material_rule = d['material_rule']
        if 'name' in d:
            o.name = d['name']
        return o


