#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TagRuleItemDTO import TagRuleItemDTO


class TagRuleGroupDTO(object):

    def __init__(self):
        self._rule_items = None

    @property
    def rule_items(self):
        return self._rule_items

    @rule_items.setter
    def rule_items(self, value):
        if isinstance(value, list):
            self._rule_items = list()
            for i in value:
                if isinstance(i, TagRuleItemDTO):
                    self._rule_items.append(i)
                else:
                    self._rule_items.append(TagRuleItemDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.rule_items:
            if isinstance(self.rule_items, list):
                for i in range(0, len(self.rule_items)):
                    element = self.rule_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rule_items[i] = element.to_alipay_dict()
            if hasattr(self.rule_items, 'to_alipay_dict'):
                params['rule_items'] = self.rule_items.to_alipay_dict()
            else:
                params['rule_items'] = self.rule_items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TagRuleGroupDTO()
        if 'rule_items' in d:
            o.rule_items = d['rule_items']
        return o


