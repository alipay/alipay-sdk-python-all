#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitSource(object):

    def __init__(self):
        self._benefit_source_type = None
        self._benefit_source_value = None

    @property
    def benefit_source_type(self):
        return self._benefit_source_type

    @benefit_source_type.setter
    def benefit_source_type(self, value):
        self._benefit_source_type = value
    @property
    def benefit_source_value(self):
        return self._benefit_source_value

    @benefit_source_value.setter
    def benefit_source_value(self, value):
        self._benefit_source_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_source_type:
            if hasattr(self.benefit_source_type, 'to_alipay_dict'):
                params['benefit_source_type'] = self.benefit_source_type.to_alipay_dict()
            else:
                params['benefit_source_type'] = self.benefit_source_type
        if self.benefit_source_value:
            if hasattr(self.benefit_source_value, 'to_alipay_dict'):
                params['benefit_source_value'] = self.benefit_source_value.to_alipay_dict()
            else:
                params['benefit_source_value'] = self.benefit_source_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitSource()
        if 'benefit_source_type' in d:
            o.benefit_source_type = d['benefit_source_type']
        if 'benefit_source_value' in d:
            o.benefit_source_value = d['benefit_source_value']
        return o


