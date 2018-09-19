#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.McardTemplateBenefit import McardTemplateBenefit


class AlipayMarketingCardBenefitCreateModel(object):

    def __init__(self):
        self._mcard_template_benefit = None

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
        o = AlipayMarketingCardBenefitCreateModel()
        if 'mcard_template_benefit' in d:
            o.mcard_template_benefit = d['mcard_template_benefit']
        return o


