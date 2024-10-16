#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DynamicRentBillingRuleMultiStageDTO import DynamicRentBillingRuleMultiStageDTO
from alipay.aop.api.domain.DynamicRentBillingRuleSingleStageDTO import DynamicRentBillingRuleSingleStageDTO


class DynamicRentBillingRuleDTO(object):

    def __init__(self):
        self._multi_stage = None
        self._single_stage = None
        self._type = None

    @property
    def multi_stage(self):
        return self._multi_stage

    @multi_stage.setter
    def multi_stage(self, value):
        if isinstance(value, DynamicRentBillingRuleMultiStageDTO):
            self._multi_stage = value
        else:
            self._multi_stage = DynamicRentBillingRuleMultiStageDTO.from_alipay_dict(value)
    @property
    def single_stage(self):
        return self._single_stage

    @single_stage.setter
    def single_stage(self, value):
        if isinstance(value, DynamicRentBillingRuleSingleStageDTO):
            self._single_stage = value
        else:
            self._single_stage = DynamicRentBillingRuleSingleStageDTO.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.multi_stage:
            if hasattr(self.multi_stage, 'to_alipay_dict'):
                params['multi_stage'] = self.multi_stage.to_alipay_dict()
            else:
                params['multi_stage'] = self.multi_stage
        if self.single_stage:
            if hasattr(self.single_stage, 'to_alipay_dict'):
                params['single_stage'] = self.single_stage.to_alipay_dict()
            else:
                params['single_stage'] = self.single_stage
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DynamicRentBillingRuleDTO()
        if 'multi_stage' in d:
            o.multi_stage = d['multi_stage']
        if 'single_stage' in d:
            o.single_stage = d['single_stage']
        if 'type' in d:
            o.type = d['type']
        return o


