#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtensionArea import ExtensionArea
from alipay.aop.api.domain.LabelRule import LabelRule


class AlipayOpenPublicPersonalizedExtensionCreateModel(object):

    def __init__(self):
        self._areas = None
        self._label_rule = None

    @property
    def areas(self):
        return self._areas

    @areas.setter
    def areas(self, value):
        if isinstance(value, list):
            self._areas = list()
            for i in value:
                if isinstance(i, ExtensionArea):
                    self._areas.append(i)
                else:
                    self._areas.append(ExtensionArea.from_alipay_dict(i))
    @property
    def label_rule(self):
        return self._label_rule

    @label_rule.setter
    def label_rule(self, value):
        if isinstance(value, list):
            self._label_rule = list()
            for i in value:
                if isinstance(i, LabelRule):
                    self._label_rule.append(i)
                else:
                    self._label_rule.append(LabelRule.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.areas:
            if isinstance(self.areas, list):
                for i in range(0, len(self.areas)):
                    element = self.areas[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.areas[i] = element.to_alipay_dict()
            if hasattr(self.areas, 'to_alipay_dict'):
                params['areas'] = self.areas.to_alipay_dict()
            else:
                params['areas'] = self.areas
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
        o = AlipayOpenPublicPersonalizedExtensionCreateModel()
        if 'areas' in d:
            o.areas = d['areas']
        if 'label_rule' in d:
            o.label_rule = d['label_rule']
        return o


