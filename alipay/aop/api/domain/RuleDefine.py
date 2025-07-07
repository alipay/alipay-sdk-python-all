#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RuleDefine(object):

    def __init__(self):
        self._biz_tids = None
        self._entity_condition = None
        self._entity_values = None

    @property
    def biz_tids(self):
        return self._biz_tids

    @biz_tids.setter
    def biz_tids(self, value):
        if isinstance(value, list):
            self._biz_tids = list()
            for i in value:
                self._biz_tids.append(i)
    @property
    def entity_condition(self):
        return self._entity_condition

    @entity_condition.setter
    def entity_condition(self, value):
        self._entity_condition = value
    @property
    def entity_values(self):
        return self._entity_values

    @entity_values.setter
    def entity_values(self, value):
        if isinstance(value, list):
            self._entity_values = list()
            for i in value:
                self._entity_values.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tids:
            if isinstance(self.biz_tids, list):
                for i in range(0, len(self.biz_tids)):
                    element = self.biz_tids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_tids[i] = element.to_alipay_dict()
            if hasattr(self.biz_tids, 'to_alipay_dict'):
                params['biz_tids'] = self.biz_tids.to_alipay_dict()
            else:
                params['biz_tids'] = self.biz_tids
        if self.entity_condition:
            if hasattr(self.entity_condition, 'to_alipay_dict'):
                params['entity_condition'] = self.entity_condition.to_alipay_dict()
            else:
                params['entity_condition'] = self.entity_condition
        if self.entity_values:
            if isinstance(self.entity_values, list):
                for i in range(0, len(self.entity_values)):
                    element = self.entity_values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entity_values[i] = element.to_alipay_dict()
            if hasattr(self.entity_values, 'to_alipay_dict'):
                params['entity_values'] = self.entity_values.to_alipay_dict()
            else:
                params['entity_values'] = self.entity_values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RuleDefine()
        if 'biz_tids' in d:
            o.biz_tids = d['biz_tids']
        if 'entity_condition' in d:
            o.entity_condition = d['entity_condition']
        if 'entity_values' in d:
            o.entity_values = d['entity_values']
        return o


