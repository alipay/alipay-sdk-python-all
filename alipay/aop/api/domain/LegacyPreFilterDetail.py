#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LegacyPreFilterValueDetail import LegacyPreFilterValueDetail


class LegacyPreFilterDetail(object):

    def __init__(self):
        self._expression_relationship = None
        self._relationship = None
        self._retrieved_column_name = None
        self._values = None

    @property
    def expression_relationship(self):
        return self._expression_relationship

    @expression_relationship.setter
    def expression_relationship(self, value):
        self._expression_relationship = value
    @property
    def relationship(self):
        return self._relationship

    @relationship.setter
    def relationship(self, value):
        self._relationship = value
    @property
    def retrieved_column_name(self):
        return self._retrieved_column_name

    @retrieved_column_name.setter
    def retrieved_column_name(self, value):
        self._retrieved_column_name = value
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        if isinstance(value, LegacyPreFilterValueDetail):
            self._values = value
        else:
            self._values = LegacyPreFilterValueDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.expression_relationship:
            if hasattr(self.expression_relationship, 'to_alipay_dict'):
                params['expression_relationship'] = self.expression_relationship.to_alipay_dict()
            else:
                params['expression_relationship'] = self.expression_relationship
        if self.relationship:
            if hasattr(self.relationship, 'to_alipay_dict'):
                params['relationship'] = self.relationship.to_alipay_dict()
            else:
                params['relationship'] = self.relationship
        if self.retrieved_column_name:
            if hasattr(self.retrieved_column_name, 'to_alipay_dict'):
                params['retrieved_column_name'] = self.retrieved_column_name.to_alipay_dict()
            else:
                params['retrieved_column_name'] = self.retrieved_column_name
        if self.values:
            if hasattr(self.values, 'to_alipay_dict'):
                params['values'] = self.values.to_alipay_dict()
            else:
                params['values'] = self.values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LegacyPreFilterDetail()
        if 'expression_relationship' in d:
            o.expression_relationship = d['expression_relationship']
        if 'relationship' in d:
            o.relationship = d['relationship']
        if 'retrieved_column_name' in d:
            o.retrieved_column_name = d['retrieved_column_name']
        if 'values' in d:
            o.values = d['values']
        return o


