#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupJoinRuleVO(object):

    def __init__(self):
        self._rule_id = None
        self._rule_type = None

    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.rule_type:
            if hasattr(self.rule_type, 'to_alipay_dict'):
                params['rule_type'] = self.rule_type.to_alipay_dict()
            else:
                params['rule_type'] = self.rule_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupJoinRuleVO()
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        return o


