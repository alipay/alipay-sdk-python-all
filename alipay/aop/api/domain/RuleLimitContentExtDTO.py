#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RuleLimitShopContentDTO import RuleLimitShopContentDTO


class RuleLimitContentExtDTO(object):

    def __init__(self):
        self._limit_type = None
        self._limit_value = None
        self._rule_limit_shop_content = None

    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value
    @property
    def limit_value(self):
        return self._limit_value

    @limit_value.setter
    def limit_value(self, value):
        self._limit_value = value
    @property
    def rule_limit_shop_content(self):
        return self._rule_limit_shop_content

    @rule_limit_shop_content.setter
    def rule_limit_shop_content(self, value):
        if isinstance(value, RuleLimitShopContentDTO):
            self._rule_limit_shop_content = value
        else:
            self._rule_limit_shop_content = RuleLimitShopContentDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        if self.limit_value:
            if hasattr(self.limit_value, 'to_alipay_dict'):
                params['limit_value'] = self.limit_value.to_alipay_dict()
            else:
                params['limit_value'] = self.limit_value
        if self.rule_limit_shop_content:
            if hasattr(self.rule_limit_shop_content, 'to_alipay_dict'):
                params['rule_limit_shop_content'] = self.rule_limit_shop_content.to_alipay_dict()
            else:
                params['rule_limit_shop_content'] = self.rule_limit_shop_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RuleLimitContentExtDTO()
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        if 'limit_value' in d:
            o.limit_value = d['limit_value']
        if 'rule_limit_shop_content' in d:
            o.rule_limit_shop_content = d['rule_limit_shop_content']
        return o


