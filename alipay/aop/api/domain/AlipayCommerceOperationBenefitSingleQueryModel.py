#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationBenefitSingleQueryModel(object):

    def __init__(self):
        self._out_benefit_id = None
        self._template_id = None

    @property
    def out_benefit_id(self):
        return self._out_benefit_id

    @out_benefit_id.setter
    def out_benefit_id(self, value):
        self._out_benefit_id = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_benefit_id:
            if hasattr(self.out_benefit_id, 'to_alipay_dict'):
                params['out_benefit_id'] = self.out_benefit_id.to_alipay_dict()
            else:
                params['out_benefit_id'] = self.out_benefit_id
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
        o = AlipayCommerceOperationBenefitSingleQueryModel()
        if 'out_benefit_id' in d:
            o.out_benefit_id = d['out_benefit_id']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


