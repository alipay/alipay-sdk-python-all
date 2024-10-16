#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiStageAmountConfigDTO import MultiStageAmountConfigDTO


class DynamicRentBillingRuleMultiStageDTO(object):

    def __init__(self):
        self._billing_cap = None
        self._stage_amount_config_list = None

    @property
    def billing_cap(self):
        return self._billing_cap

    @billing_cap.setter
    def billing_cap(self, value):
        self._billing_cap = value
    @property
    def stage_amount_config_list(self):
        return self._stage_amount_config_list

    @stage_amount_config_list.setter
    def stage_amount_config_list(self, value):
        if isinstance(value, list):
            self._stage_amount_config_list = list()
            for i in value:
                if isinstance(i, MultiStageAmountConfigDTO):
                    self._stage_amount_config_list.append(i)
                else:
                    self._stage_amount_config_list.append(MultiStageAmountConfigDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.billing_cap:
            if hasattr(self.billing_cap, 'to_alipay_dict'):
                params['billing_cap'] = self.billing_cap.to_alipay_dict()
            else:
                params['billing_cap'] = self.billing_cap
        if self.stage_amount_config_list:
            if isinstance(self.stage_amount_config_list, list):
                for i in range(0, len(self.stage_amount_config_list)):
                    element = self.stage_amount_config_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stage_amount_config_list[i] = element.to_alipay_dict()
            if hasattr(self.stage_amount_config_list, 'to_alipay_dict'):
                params['stage_amount_config_list'] = self.stage_amount_config_list.to_alipay_dict()
            else:
                params['stage_amount_config_list'] = self.stage_amount_config_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DynamicRentBillingRuleMultiStageDTO()
        if 'billing_cap' in d:
            o.billing_cap = d['billing_cap']
        if 'stage_amount_config_list' in d:
            o.stage_amount_config_list = d['stage_amount_config_list']
        return o


