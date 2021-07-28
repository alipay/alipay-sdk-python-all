#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishCommRuleInfo import KbdishCommRuleInfo


class KoubeiCateringDishCommruleSyncModel(object):

    def __init__(self):
        self._kbdish_comm_rule_info_list = None

    @property
    def kbdish_comm_rule_info_list(self):
        return self._kbdish_comm_rule_info_list

    @kbdish_comm_rule_info_list.setter
    def kbdish_comm_rule_info_list(self, value):
        if isinstance(value, list):
            self._kbdish_comm_rule_info_list = list()
            for i in value:
                if isinstance(i, KbdishCommRuleInfo):
                    self._kbdish_comm_rule_info_list.append(i)
                else:
                    self._kbdish_comm_rule_info_list.append(KbdishCommRuleInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.kbdish_comm_rule_info_list:
            if isinstance(self.kbdish_comm_rule_info_list, list):
                for i in range(0, len(self.kbdish_comm_rule_info_list)):
                    element = self.kbdish_comm_rule_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.kbdish_comm_rule_info_list[i] = element.to_alipay_dict()
            if hasattr(self.kbdish_comm_rule_info_list, 'to_alipay_dict'):
                params['kbdish_comm_rule_info_list'] = self.kbdish_comm_rule_info_list.to_alipay_dict()
            else:
                params['kbdish_comm_rule_info_list'] = self.kbdish_comm_rule_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishCommruleSyncModel()
        if 'kbdish_comm_rule_info_list' in d:
            o.kbdish_comm_rule_info_list = d['kbdish_comm_rule_info_list']
        return o


