#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitEnrollMerchant import RecruitEnrollMerchant


class AlipayMarketingRecruitPlanQueryModel(object):

    def __init__(self):
        self._enroll_merchant = None
        self._plan_id = None

    @property
    def enroll_merchant(self):
        return self._enroll_merchant

    @enroll_merchant.setter
    def enroll_merchant(self, value):
        if isinstance(value, RecruitEnrollMerchant):
            self._enroll_merchant = value
        else:
            self._enroll_merchant = RecruitEnrollMerchant.from_alipay_dict(value)
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enroll_merchant:
            if hasattr(self.enroll_merchant, 'to_alipay_dict'):
                params['enroll_merchant'] = self.enroll_merchant.to_alipay_dict()
            else:
                params['enroll_merchant'] = self.enroll_merchant
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingRecruitPlanQueryModel()
        if 'enroll_merchant' in d:
            o.enroll_merchant = d['enroll_merchant']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        return o


