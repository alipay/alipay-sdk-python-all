#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RuleInfo import RuleInfo


class RuleQueryResult(object):

    def __init__(self):
        self._rule_info_list = None

    @property
    def rule_info_list(self):
        return self._rule_info_list

    @rule_info_list.setter
    def rule_info_list(self, value):
        if isinstance(value, list):
            self._rule_info_list = list()
            for i in value:
                if isinstance(i, RuleInfo):
                    self._rule_info_list.append(i)
                else:
                    self._rule_info_list.append(RuleInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.rule_info_list:
            if isinstance(self.rule_info_list, list):
                for i in range(0, len(self.rule_info_list)):
                    element = self.rule_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rule_info_list[i] = element.to_alipay_dict()
            if hasattr(self.rule_info_list, 'to_alipay_dict'):
                params['rule_info_list'] = self.rule_info_list.to_alipay_dict()
            else:
                params['rule_info_list'] = self.rule_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RuleQueryResult()
        if 'rule_info_list' in d:
            o.rule_info_list = d['rule_info_list']
        return o


