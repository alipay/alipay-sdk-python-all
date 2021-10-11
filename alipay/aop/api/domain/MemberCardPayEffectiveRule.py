#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MemberCardPayEffectiveItemRule import MemberCardPayEffectiveItemRule
from alipay.aop.api.domain.MemberCardPayEffectiveShopRule import MemberCardPayEffectiveShopRule


class MemberCardPayEffectiveRule(object):

    def __init__(self):
        self._item_rule = None
        self._shop_rules = None
        self._smids = None

    @property
    def item_rule(self):
        return self._item_rule

    @item_rule.setter
    def item_rule(self, value):
        if isinstance(value, MemberCardPayEffectiveItemRule):
            self._item_rule = value
        else:
            self._item_rule = MemberCardPayEffectiveItemRule.from_alipay_dict(value)
    @property
    def shop_rules(self):
        return self._shop_rules

    @shop_rules.setter
    def shop_rules(self, value):
        if isinstance(value, list):
            self._shop_rules = list()
            for i in value:
                if isinstance(i, MemberCardPayEffectiveShopRule):
                    self._shop_rules.append(i)
                else:
                    self._shop_rules.append(MemberCardPayEffectiveShopRule.from_alipay_dict(i))
    @property
    def smids(self):
        return self._smids

    @smids.setter
    def smids(self, value):
        if isinstance(value, list):
            self._smids = list()
            for i in value:
                self._smids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.item_rule:
            if hasattr(self.item_rule, 'to_alipay_dict'):
                params['item_rule'] = self.item_rule.to_alipay_dict()
            else:
                params['item_rule'] = self.item_rule
        if self.shop_rules:
            if isinstance(self.shop_rules, list):
                for i in range(0, len(self.shop_rules)):
                    element = self.shop_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_rules[i] = element.to_alipay_dict()
            if hasattr(self.shop_rules, 'to_alipay_dict'):
                params['shop_rules'] = self.shop_rules.to_alipay_dict()
            else:
                params['shop_rules'] = self.shop_rules
        if self.smids:
            if isinstance(self.smids, list):
                for i in range(0, len(self.smids)):
                    element = self.smids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.smids[i] = element.to_alipay_dict()
            if hasattr(self.smids, 'to_alipay_dict'):
                params['smids'] = self.smids.to_alipay_dict()
            else:
                params['smids'] = self.smids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberCardPayEffectiveRule()
        if 'item_rule' in d:
            o.item_rule = d['item_rule']
        if 'shop_rules' in d:
            o.shop_rules = d['shop_rules']
        if 'smids' in d:
            o.smids = d['smids']
        return o


