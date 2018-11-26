#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishRuleInfo import KbdishRuleInfo


class KoubeiCateringDishRuleModifyModel(object):

    def __init__(self):
        self._kb_dish_rule_info = None

    @property
    def kb_dish_rule_info(self):
        return self._kb_dish_rule_info

    @kb_dish_rule_info.setter
    def kb_dish_rule_info(self, value):
        if isinstance(value, KbdishRuleInfo):
            self._kb_dish_rule_info = value
        else:
            self._kb_dish_rule_info = KbdishRuleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.kb_dish_rule_info:
            if hasattr(self.kb_dish_rule_info, 'to_alipay_dict'):
                params['kb_dish_rule_info'] = self.kb_dish_rule_info.to_alipay_dict()
            else:
                params['kb_dish_rule_info'] = self.kb_dish_rule_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishRuleModifyModel()
        if 'kb_dish_rule_info' in d:
            o.kb_dish_rule_info = d['kb_dish_rule_info']
        return o


