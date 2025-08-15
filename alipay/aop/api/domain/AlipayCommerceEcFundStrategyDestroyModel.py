#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcFundStrategyDestroyModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._strategy_id = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def strategy_id(self):
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, value):
        self._strategy_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.strategy_id:
            if hasattr(self.strategy_id, 'to_alipay_dict'):
                params['strategy_id'] = self.strategy_id.to_alipay_dict()
            else:
                params['strategy_id'] = self.strategy_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcFundStrategyDestroyModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'strategy_id' in d:
            o.strategy_id = d['strategy_id']
        return o


