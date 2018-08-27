#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QueryComplexLabelRule import QueryComplexLabelRule


class QueryGroup(object):

    def __init__(self):
        self._id = None
        self._label_rule = None
        self._name = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def label_rule(self):
        return self._label_rule

    @label_rule.setter
    def label_rule(self, value):
        if isinstance(value, list):
            self._label_rule = list()
            for i in value:
                if isinstance(i, QueryComplexLabelRule):
                    self._label_rule.append(i)
                else:
                    self._label_rule.append(QueryComplexLabelRule.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryGroup()
        if 'id' in d:
            o.id = d['id']
        if 'label_rule' in d:
            o.label_rule = d['label_rule']
        if 'name' in d:
            o.name = d['name']
        return o


