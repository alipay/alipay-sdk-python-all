#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradingStageDTO import TradingStageDTO


class TradingPeriodDTO(object):

    def __init__(self):
        self._belong_day = None
        self._stages = None

    @property
    def belong_day(self):
        return self._belong_day

    @belong_day.setter
    def belong_day(self, value):
        self._belong_day = value
    @property
    def stages(self):
        return self._stages

    @stages.setter
    def stages(self, value):
        if isinstance(value, list):
            self._stages = list()
            for i in value:
                if isinstance(i, TradingStageDTO):
                    self._stages.append(i)
                else:
                    self._stages.append(TradingStageDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.belong_day:
            if hasattr(self.belong_day, 'to_alipay_dict'):
                params['belong_day'] = self.belong_day.to_alipay_dict()
            else:
                params['belong_day'] = self.belong_day
        if self.stages:
            if isinstance(self.stages, list):
                for i in range(0, len(self.stages)):
                    element = self.stages[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stages[i] = element.to_alipay_dict()
            if hasattr(self.stages, 'to_alipay_dict'):
                params['stages'] = self.stages.to_alipay_dict()
            else:
                params['stages'] = self.stages
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradingPeriodDTO()
        if 'belong_day' in d:
            o.belong_day = d['belong_day']
        if 'stages' in d:
            o.stages = d['stages']
        return o


