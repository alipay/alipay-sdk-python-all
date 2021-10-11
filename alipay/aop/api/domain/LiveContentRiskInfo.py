#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LiveContentRiskInfo(object):

    def __init__(self):
        self._risk_infos = None
        self._risk_level = None
        self._risk_tips = None
        self._rule_code = None
        self._rule_name = None

    @property
    def risk_infos(self):
        return self._risk_infos

    @risk_infos.setter
    def risk_infos(self, value):
        self._risk_infos = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def risk_tips(self):
        return self._risk_tips

    @risk_tips.setter
    def risk_tips(self, value):
        self._risk_tips = value
    @property
    def rule_code(self):
        return self._rule_code

    @rule_code.setter
    def rule_code(self, value):
        self._rule_code = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_infos:
            if hasattr(self.risk_infos, 'to_alipay_dict'):
                params['risk_infos'] = self.risk_infos.to_alipay_dict()
            else:
                params['risk_infos'] = self.risk_infos
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.risk_tips:
            if hasattr(self.risk_tips, 'to_alipay_dict'):
                params['risk_tips'] = self.risk_tips.to_alipay_dict()
            else:
                params['risk_tips'] = self.risk_tips
        if self.rule_code:
            if hasattr(self.rule_code, 'to_alipay_dict'):
                params['rule_code'] = self.rule_code.to_alipay_dict()
            else:
                params['rule_code'] = self.rule_code
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LiveContentRiskInfo()
        if 'risk_infos' in d:
            o.risk_infos = d['risk_infos']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'risk_tips' in d:
            o.risk_tips = d['risk_tips']
        if 'rule_code' in d:
            o.rule_code = d['rule_code']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        return o


