#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ComplexLabelRule import ComplexLabelRule


class AlipayOpenPublicGroupCrowdQueryModel(object):

    def __init__(self):
        self._label_rule = None

    @property
    def label_rule(self):
        return self._label_rule

    @label_rule.setter
    def label_rule(self, value):
        if isinstance(value, list):
            self._label_rule = list()
            for i in value:
                if isinstance(i, ComplexLabelRule):
                    self._label_rule.append(i)
                else:
                    self._label_rule.append(ComplexLabelRule.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.label_rule:
            if isinstance(self.label_rule, list):
                for i in range(0, len(self.label_rule)):
                    element = self.label_rule[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label_rule[i] = element.to_alipay_dict()
            if hasattr(self.label_rule, 'to_alipay_dict'):
                params['label_rule'] = self.label_rule.to_alipay_dict()
            else:
                params['label_rule'] = self.label_rule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicGroupCrowdQueryModel()
        if 'label_rule' in d:
            o.label_rule = d['label_rule']
        return o


