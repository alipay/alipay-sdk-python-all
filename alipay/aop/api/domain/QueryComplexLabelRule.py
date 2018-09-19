#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryComplexLabelRule(object):

    def __init__(self):
        self._label_id = None
        self._label_name = None
        self._label_value = None
        self._operator = None

    @property
    def label_id(self):
        return self._label_id

    @label_id.setter
    def label_id(self, value):
        self._label_id = value
    @property
    def label_name(self):
        return self._label_name

    @label_name.setter
    def label_name(self, value):
        self._label_name = value
    @property
    def label_value(self):
        return self._label_value

    @label_value.setter
    def label_value(self, value):
        self._label_value = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value


    def to_alipay_dict(self):
        params = dict()
        if self.label_id:
            if hasattr(self.label_id, 'to_alipay_dict'):
                params['label_id'] = self.label_id.to_alipay_dict()
            else:
                params['label_id'] = self.label_id
        if self.label_name:
            if hasattr(self.label_name, 'to_alipay_dict'):
                params['label_name'] = self.label_name.to_alipay_dict()
            else:
                params['label_name'] = self.label_name
        if self.label_value:
            if hasattr(self.label_value, 'to_alipay_dict'):
                params['label_value'] = self.label_value.to_alipay_dict()
            else:
                params['label_value'] = self.label_value
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryComplexLabelRule()
        if 'label_id' in d:
            o.label_id = d['label_id']
        if 'label_name' in d:
            o.label_name = d['label_name']
        if 'label_value' in d:
            o.label_value = d['label_value']
        if 'operator' in d:
            o.operator = d['operator']
        return o


