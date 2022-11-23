#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelBenefitbudgetQueryModel(object):

    def __init__(self):
        self._benefit_ids = None

    @property
    def benefit_ids(self):
        return self._benefit_ids

    @benefit_ids.setter
    def benefit_ids(self, value):
        if isinstance(value, list):
            self._benefit_ids = list()
            for i in value:
                self._benefit_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_ids:
            if isinstance(self.benefit_ids, list):
                for i in range(0, len(self.benefit_ids)):
                    element = self.benefit_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_ids[i] = element.to_alipay_dict()
            if hasattr(self.benefit_ids, 'to_alipay_dict'):
                params['benefit_ids'] = self.benefit_ids.to_alipay_dict()
            else:
                params['benefit_ids'] = self.benefit_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelBenefitbudgetQueryModel()
        if 'benefit_ids' in d:
            o.benefit_ids = d['benefit_ids']
        return o


