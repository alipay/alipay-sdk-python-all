#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiAuthAmountDTO import OpenApiAuthAmountDTO


class OpenApiAuthAmountInfoDTO(object):

    def __init__(self):
        self._amounts = None
        self._rule_code = None
        self._rule_name = None

    @property
    def amounts(self):
        return self._amounts

    @amounts.setter
    def amounts(self, value):
        if isinstance(value, list):
            self._amounts = list()
            for i in value:
                if isinstance(i, OpenApiAuthAmountDTO):
                    self._amounts.append(i)
                else:
                    self._amounts.append(OpenApiAuthAmountDTO.from_alipay_dict(i))
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
        if self.amounts:
            if isinstance(self.amounts, list):
                for i in range(0, len(self.amounts)):
                    element = self.amounts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.amounts[i] = element.to_alipay_dict()
            if hasattr(self.amounts, 'to_alipay_dict'):
                params['amounts'] = self.amounts.to_alipay_dict()
            else:
                params['amounts'] = self.amounts
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
        o = OpenApiAuthAmountInfoDTO()
        if 'amounts' in d:
            o.amounts = d['amounts']
        if 'rule_code' in d:
            o.rule_code = d['rule_code']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        return o


