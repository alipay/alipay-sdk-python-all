#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantGroupGroupcontrolGroupModifyModel(object):

    def __init__(self):
        self._global_valid = None
        self._group_id_list = None
        self._rule_id = None

    @property
    def global_valid(self):
        return self._global_valid

    @global_valid.setter
    def global_valid(self, value):
        self._global_valid = value
    @property
    def group_id_list(self):
        return self._group_id_list

    @group_id_list.setter
    def group_id_list(self, value):
        if isinstance(value, list):
            self._group_id_list = list()
            for i in value:
                self._group_id_list.append(i)
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.global_valid:
            if hasattr(self.global_valid, 'to_alipay_dict'):
                params['global_valid'] = self.global_valid.to_alipay_dict()
            else:
                params['global_valid'] = self.global_valid
        if self.group_id_list:
            if isinstance(self.group_id_list, list):
                for i in range(0, len(self.group_id_list)):
                    element = self.group_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_id_list[i] = element.to_alipay_dict()
            if hasattr(self.group_id_list, 'to_alipay_dict'):
                params['group_id_list'] = self.group_id_list.to_alipay_dict()
            else:
                params['group_id_list'] = self.group_id_list
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupGroupcontrolGroupModifyModel()
        if 'global_valid' in d:
            o.global_valid = d['global_valid']
        if 'group_id_list' in d:
            o.group_id_list = d['group_id_list']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        return o


