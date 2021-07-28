#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstalmentPlanTuitionDTO import InstalmentPlanTuitionDTO
from alipay.aop.api.domain.RechargeOrderTuitionDTO import RechargeOrderTuitionDTO


class InstalmentPlanDetailTuitionDTO(object):

    def __init__(self):
        self._plan = None
        self._recharge_order = None

    @property
    def plan(self):
        return self._plan

    @plan.setter
    def plan(self, value):
        if isinstance(value, InstalmentPlanTuitionDTO):
            self._plan = value
        else:
            self._plan = InstalmentPlanTuitionDTO.from_alipay_dict(value)
    @property
    def recharge_order(self):
        return self._recharge_order

    @recharge_order.setter
    def recharge_order(self, value):
        if isinstance(value, RechargeOrderTuitionDTO):
            self._recharge_order = value
        else:
            self._recharge_order = RechargeOrderTuitionDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.plan:
            if hasattr(self.plan, 'to_alipay_dict'):
                params['plan'] = self.plan.to_alipay_dict()
            else:
                params['plan'] = self.plan
        if self.recharge_order:
            if hasattr(self.recharge_order, 'to_alipay_dict'):
                params['recharge_order'] = self.recharge_order.to_alipay_dict()
            else:
                params['recharge_order'] = self.recharge_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstalmentPlanDetailTuitionDTO()
        if 'plan' in d:
            o.plan = d['plan']
        if 'recharge_order' in d:
            o.recharge_order = d['recharge_order']
        return o


