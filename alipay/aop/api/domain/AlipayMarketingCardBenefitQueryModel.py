#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCardBenefitQueryModel(object):

    def __init__(self):
        self._benefit_id = None
        self._template_id = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCardBenefitQueryModel()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


