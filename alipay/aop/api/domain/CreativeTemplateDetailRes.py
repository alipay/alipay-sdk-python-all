#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InfraTemplateEnumRuleResp import InfraTemplateEnumRuleResp
from alipay.aop.api.domain.InfraTemplateMoneyRuleResp import InfraTemplateMoneyRuleResp
from alipay.aop.api.domain.InfraTemplateRuleResp import InfraTemplateRuleResp


class CreativeTemplateDetailRes(object):

    def __init__(self):
        self._desc = None
        self._enum_rules = None
        self._key = None
        self._max_num = None
        self._money_rules = None
        self._need = None
        self._rules = None
        self._show_name = None
        self._type = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def enum_rules(self):
        return self._enum_rules

    @enum_rules.setter
    def enum_rules(self, value):
        if isinstance(value, list):
            self._enum_rules = list()
            for i in value:
                if isinstance(i, InfraTemplateEnumRuleResp):
                    self._enum_rules.append(i)
                else:
                    self._enum_rules.append(InfraTemplateEnumRuleResp.from_alipay_dict(i))
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def max_num(self):
        return self._max_num

    @max_num.setter
    def max_num(self, value):
        self._max_num = value
    @property
    def money_rules(self):
        return self._money_rules

    @money_rules.setter
    def money_rules(self, value):
        if isinstance(value, list):
            self._money_rules = list()
            for i in value:
                if isinstance(i, InfraTemplateMoneyRuleResp):
                    self._money_rules.append(i)
                else:
                    self._money_rules.append(InfraTemplateMoneyRuleResp.from_alipay_dict(i))
    @property
    def need(self):
        return self._need

    @need.setter
    def need(self, value):
        self._need = value
    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, value):
        if isinstance(value, list):
            self._rules = list()
            for i in value:
                if isinstance(i, InfraTemplateRuleResp):
                    self._rules.append(i)
                else:
                    self._rules.append(InfraTemplateRuleResp.from_alipay_dict(i))
    @property
    def show_name(self):
        return self._show_name

    @show_name.setter
    def show_name(self, value):
        self._show_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.enum_rules:
            if isinstance(self.enum_rules, list):
                for i in range(0, len(self.enum_rules)):
                    element = self.enum_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.enum_rules[i] = element.to_alipay_dict()
            if hasattr(self.enum_rules, 'to_alipay_dict'):
                params['enum_rules'] = self.enum_rules.to_alipay_dict()
            else:
                params['enum_rules'] = self.enum_rules
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.max_num:
            if hasattr(self.max_num, 'to_alipay_dict'):
                params['max_num'] = self.max_num.to_alipay_dict()
            else:
                params['max_num'] = self.max_num
        if self.money_rules:
            if isinstance(self.money_rules, list):
                for i in range(0, len(self.money_rules)):
                    element = self.money_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.money_rules[i] = element.to_alipay_dict()
            if hasattr(self.money_rules, 'to_alipay_dict'):
                params['money_rules'] = self.money_rules.to_alipay_dict()
            else:
                params['money_rules'] = self.money_rules
        if self.need:
            if hasattr(self.need, 'to_alipay_dict'):
                params['need'] = self.need.to_alipay_dict()
            else:
                params['need'] = self.need
        if self.rules:
            if isinstance(self.rules, list):
                for i in range(0, len(self.rules)):
                    element = self.rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rules[i] = element.to_alipay_dict()
            if hasattr(self.rules, 'to_alipay_dict'):
                params['rules'] = self.rules.to_alipay_dict()
            else:
                params['rules'] = self.rules
        if self.show_name:
            if hasattr(self.show_name, 'to_alipay_dict'):
                params['show_name'] = self.show_name.to_alipay_dict()
            else:
                params['show_name'] = self.show_name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreativeTemplateDetailRes()
        if 'desc' in d:
            o.desc = d['desc']
        if 'enum_rules' in d:
            o.enum_rules = d['enum_rules']
        if 'key' in d:
            o.key = d['key']
        if 'max_num' in d:
            o.max_num = d['max_num']
        if 'money_rules' in d:
            o.money_rules = d['money_rules']
        if 'need' in d:
            o.need = d['need']
        if 'rules' in d:
            o.rules = d['rules']
        if 'show_name' in d:
            o.show_name = d['show_name']
        if 'type' in d:
            o.type = d['type']
        return o


