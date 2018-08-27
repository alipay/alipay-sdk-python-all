#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstallmentMetaInfo import InstallmentMetaInfo


class InstallmentValue(object):

    def __init__(self):
        self._installment_values = None

    @property
    def installment_values(self):
        return self._installment_values

    @installment_values.setter
    def installment_values(self, value):
        if isinstance(value, list):
            self._installment_values = list()
            for i in value:
                if isinstance(i, InstallmentMetaInfo):
                    self._installment_values.append(i)
                else:
                    self._installment_values.append(InstallmentMetaInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.installment_values:
            if isinstance(self.installment_values, list):
                for i in range(0, len(self.installment_values)):
                    element = self.installment_values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.installment_values[i] = element.to_alipay_dict()
            if hasattr(self.installment_values, 'to_alipay_dict'):
                params['installment_values'] = self.installment_values.to_alipay_dict()
            else:
                params['installment_values'] = self.installment_values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstallmentValue()
        if 'installment_values' in d:
            o.installment_values = d['installment_values']
        return o


