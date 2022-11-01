#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAutocheckTaskTriggerModel(object):

    def __init__(self):
        self._case_id = None
        self._strategy_id = None
        self._trigger = None

    @property
    def case_id(self):
        return self._case_id

    @case_id.setter
    def case_id(self, value):
        self._case_id = value
    @property
    def strategy_id(self):
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, value):
        self._strategy_id = value
    @property
    def trigger(self):
        return self._trigger

    @trigger.setter
    def trigger(self, value):
        self._trigger = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_id:
            if hasattr(self.case_id, 'to_alipay_dict'):
                params['case_id'] = self.case_id.to_alipay_dict()
            else:
                params['case_id'] = self.case_id
        if self.strategy_id:
            if hasattr(self.strategy_id, 'to_alipay_dict'):
                params['strategy_id'] = self.strategy_id.to_alipay_dict()
            else:
                params['strategy_id'] = self.strategy_id
        if self.trigger:
            if hasattr(self.trigger, 'to_alipay_dict'):
                params['trigger'] = self.trigger.to_alipay_dict()
            else:
                params['trigger'] = self.trigger
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAutocheckTaskTriggerModel()
        if 'case_id' in d:
            o.case_id = d['case_id']
        if 'strategy_id' in d:
            o.strategy_id = d['strategy_id']
        if 'trigger' in d:
            o.trigger = d['trigger']
        return o


