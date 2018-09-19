#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.McardTemplateBenefit import McardTemplateBenefit


class AlipayMarketingCardBenefitModifyModel(object):

    def __init__(self):
        self._benefit_id = None
        self._mcard_template_benefit = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def mcard_template_benefit(self):
        return self._mcard_template_benefit

    @mcard_template_benefit.setter
    def mcard_template_benefit(self, value):
        if isinstance(value, McardTemplateBenefit):
            self._mcard_template_benefit = value
        else:
            self._mcard_template_benefit = McardTemplateBenefit.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.mcard_template_benefit:
            if hasattr(self.mcard_template_benefit, 'to_alipay_dict'):
                params['mcard_template_benefit'] = self.mcard_template_benefit.to_alipay_dict()
            else:
                params['mcard_template_benefit'] = self.mcard_template_benefit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCardBenefitModifyModel()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'mcard_template_benefit' in d:
            o.mcard_template_benefit = d['mcard_template_benefit']
        return o


