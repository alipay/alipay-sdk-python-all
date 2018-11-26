#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdPlan import AdPlan


class AlipayCommerceTransportAdPlanCreateModel(object):

    def __init__(self):
        self._ad_plan = None

    @property
    def ad_plan(self):
        return self._ad_plan

    @ad_plan.setter
    def ad_plan(self, value):
        if isinstance(value, AdPlan):
            self._ad_plan = value
        else:
            self._ad_plan = AdPlan.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ad_plan:
            if hasattr(self.ad_plan, 'to_alipay_dict'):
                params['ad_plan'] = self.ad_plan.to_alipay_dict()
            else:
                params['ad_plan'] = self.ad_plan
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportAdPlanCreateModel()
        if 'ad_plan' in d:
            o.ad_plan = d['ad_plan']
        return o


