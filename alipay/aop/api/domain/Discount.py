#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitAmount import BenefitAmount
from alipay.aop.api.domain.Benefit import Benefit


class Discount(object):

    def __init__(self):
        self._benefit_amounts = None
        self._benefit_desc = None
        self._benefit_money = None
        self._benefit_service = None
        self._cost = None
        self._name = None
        self._rule_desc = None
        self._type = None

    @property
    def benefit_amounts(self):
        return self._benefit_amounts

    @benefit_amounts.setter
    def benefit_amounts(self, value):
        if isinstance(value, list):
            self._benefit_amounts = list()
            for i in value:
                if isinstance(i, BenefitAmount):
                    self._benefit_amounts.append(i)
                else:
                    self._benefit_amounts.append(BenefitAmount.from_alipay_dict(i))
    @property
    def benefit_desc(self):
        return self._benefit_desc

    @benefit_desc.setter
    def benefit_desc(self, value):
        self._benefit_desc = value
    @property
    def benefit_money(self):
        return self._benefit_money

    @benefit_money.setter
    def benefit_money(self, value):
        self._benefit_money = value
    @property
    def benefit_service(self):
        return self._benefit_service

    @benefit_service.setter
    def benefit_service(self, value):
        if isinstance(value, list):
            self._benefit_service = list()
            for i in value:
                if isinstance(i, Benefit):
                    self._benefit_service.append(i)
                else:
                    self._benefit_service.append(Benefit.from_alipay_dict(i))
    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def rule_desc(self):
        return self._rule_desc

    @rule_desc.setter
    def rule_desc(self, value):
        self._rule_desc = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_amounts:
            if isinstance(self.benefit_amounts, list):
                for i in range(0, len(self.benefit_amounts)):
                    element = self.benefit_amounts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_amounts[i] = element.to_alipay_dict()
            if hasattr(self.benefit_amounts, 'to_alipay_dict'):
                params['benefit_amounts'] = self.benefit_amounts.to_alipay_dict()
            else:
                params['benefit_amounts'] = self.benefit_amounts
        if self.benefit_desc:
            if hasattr(self.benefit_desc, 'to_alipay_dict'):
                params['benefit_desc'] = self.benefit_desc.to_alipay_dict()
            else:
                params['benefit_desc'] = self.benefit_desc
        if self.benefit_money:
            if hasattr(self.benefit_money, 'to_alipay_dict'):
                params['benefit_money'] = self.benefit_money.to_alipay_dict()
            else:
                params['benefit_money'] = self.benefit_money
        if self.benefit_service:
            if isinstance(self.benefit_service, list):
                for i in range(0, len(self.benefit_service)):
                    element = self.benefit_service[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_service[i] = element.to_alipay_dict()
            if hasattr(self.benefit_service, 'to_alipay_dict'):
                params['benefit_service'] = self.benefit_service.to_alipay_dict()
            else:
                params['benefit_service'] = self.benefit_service
        if self.cost:
            if hasattr(self.cost, 'to_alipay_dict'):
                params['cost'] = self.cost.to_alipay_dict()
            else:
                params['cost'] = self.cost
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.rule_desc:
            if hasattr(self.rule_desc, 'to_alipay_dict'):
                params['rule_desc'] = self.rule_desc.to_alipay_dict()
            else:
                params['rule_desc'] = self.rule_desc
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
        o = Discount()
        if 'benefit_amounts' in d:
            o.benefit_amounts = d['benefit_amounts']
        if 'benefit_desc' in d:
            o.benefit_desc = d['benefit_desc']
        if 'benefit_money' in d:
            o.benefit_money = d['benefit_money']
        if 'benefit_service' in d:
            o.benefit_service = d['benefit_service']
        if 'cost' in d:
            o.cost = d['cost']
        if 'name' in d:
            o.name = d['name']
        if 'rule_desc' in d:
            o.rule_desc = d['rule_desc']
        if 'type' in d:
            o.type = d['type']
        return o


