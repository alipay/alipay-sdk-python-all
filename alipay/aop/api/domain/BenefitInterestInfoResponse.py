#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitInterestInfoResponse(object):

    def __init__(self):
        self._benefit_description = None
        self._benefit_type = None
        self._benefit_value = None

    @property
    def benefit_description(self):
        return self._benefit_description

    @benefit_description.setter
    def benefit_description(self, value):
        self._benefit_description = value
    @property
    def benefit_type(self):
        return self._benefit_type

    @benefit_type.setter
    def benefit_type(self, value):
        self._benefit_type = value
    @property
    def benefit_value(self):
        return self._benefit_value

    @benefit_value.setter
    def benefit_value(self, value):
        self._benefit_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_description:
            if hasattr(self.benefit_description, 'to_alipay_dict'):
                params['benefit_description'] = self.benefit_description.to_alipay_dict()
            else:
                params['benefit_description'] = self.benefit_description
        if self.benefit_type:
            if hasattr(self.benefit_type, 'to_alipay_dict'):
                params['benefit_type'] = self.benefit_type.to_alipay_dict()
            else:
                params['benefit_type'] = self.benefit_type
        if self.benefit_value:
            if hasattr(self.benefit_value, 'to_alipay_dict'):
                params['benefit_value'] = self.benefit_value.to_alipay_dict()
            else:
                params['benefit_value'] = self.benefit_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitInterestInfoResponse()
        if 'benefit_description' in d:
            o.benefit_description = d['benefit_description']
        if 'benefit_type' in d:
            o.benefit_type = d['benefit_type']
        if 'benefit_value' in d:
            o.benefit_value = d['benefit_value']
        return o


