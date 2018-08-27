#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingToolFengdieSpaceQueryModel(object):

    def __init__(self):
        self._operator = None
        self._space_id = None

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def space_id(self):
        return self._space_id

    @space_id.setter
    def space_id(self, value):
        self._space_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.space_id:
            if hasattr(self.space_id, 'to_alipay_dict'):
                params['space_id'] = self.space_id.to_alipay_dict()
            else:
                params['space_id'] = self.space_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingToolFengdieSpaceQueryModel()
        if 'operator' in d:
            o.operator = d['operator']
        if 'space_id' in d:
            o.space_id = d['space_id']
        return o


