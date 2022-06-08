#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TagRuleGroupDTO import TagRuleGroupDTO


class DatadigitalFincloudFinsaasTagcrowdCountQueryModel(object):

    def __init__(self):
        self._rules = None
        self._scene_code = None

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, value):
        if isinstance(value, list):
            self._rules = list()
            for i in value:
                if isinstance(i, TagRuleGroupDTO):
                    self._rules.append(i)
                else:
                    self._rules.append(TagRuleGroupDTO.from_alipay_dict(i))
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.rules:
            if isinstance(self.rules, list):
                for i in range(0, len(self.rules)):
                    element = self.rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rules[i] = element.to_alipay_dict()
            if hasattr(self.rules, 'to_alipay_dict'):
                params['rules'] = self.rules.to_alipay_dict()
            else:
                params['rules'] = self.rules
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasTagcrowdCountQueryModel()
        if 'rules' in d:
            o.rules = d['rules']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


