#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccessCheckItemInfo(object):

    def __init__(self):
        self._access_check = None
        self._rule_id = None
        self._rule_name = None
        self._tips = None

    @property
    def access_check(self):
        return self._access_check

    @access_check.setter
    def access_check(self, value):
        self._access_check = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        self._tips = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_check:
            if hasattr(self.access_check, 'to_alipay_dict'):
                params['access_check'] = self.access_check.to_alipay_dict()
            else:
                params['access_check'] = self.access_check
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        if self.tips:
            if hasattr(self.tips, 'to_alipay_dict'):
                params['tips'] = self.tips.to_alipay_dict()
            else:
                params['tips'] = self.tips
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessCheckItemInfo()
        if 'access_check' in d:
            o.access_check = d['access_check']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'tips' in d:
            o.tips = d['tips']
        return o


